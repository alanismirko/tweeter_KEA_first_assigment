from bottle import post, request, redirect, view
import g
import mysql.connector


@post("/tweet_update/<tweet_id_update>")
@view("index")
def _(tweet_id_update):
    
    try:
        tweet_id_update = request.forms.get("tweet_id_update")
        tweet_title_update = request.forms.get("tweet_title_update")
        tweet_description_update = request.forms.get("tweet_description_update")
        tweet_created_at_update = request.forms.get("tweet_created_at_update")
        tweet_updated_at_update = request.forms.get("tweet_updated_at_update")
        user_session_id = request.get_cookie("uuid4")
        tweet_user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)

        tweet = {
            "tweet_id": tweet_id_update, 
            "tweet_title": tweet_title_update, 
            "tweet_description":tweet_description_update,
            "tweet_created_at": tweet_created_at_update,
            "tweet_updated_at": tweet_updated_at_update,
            "tweet_user_email": tweet_user_email
            }

        if len(tweet_title_update) < 1:
            return redirect(f"/index?error=tweet_title&tweet_description={tweet_description_update}")
        if len(tweet_description_update) < 1:
            return redirect(f"/index?error=tweet_description&tweet_title={tweet_title_update}")

        if user_session_id not in g.SESSIONS:
             return redirect("/login")
             
        db_config = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        sql = """SELECT * FROM tweets  WHERE tweet_id =%s """
        cursor.execute(sql, (tweet_id_update,))


        sql = """ UPDATE tweets
                SET tweet_title =%s,
                tweet_description =%s,
                tweet_created_at_update =%s,
                tweet_updated_at_update =%s,
                tweet_user_email =%s
                WHERE tweet_id =%s"""
        cursor.execute(sql, (tweet_title_update,tweet_description_update, tweet_id_update,tweet_created_at_update,tweet_updated_at_update, tweet_user_email,))
        db.commit()
        print("tweet is updated", tweet)

    except Exception as ex:
        print(ex)
    finally:
        db.close()

    
    return redirect("/index")


