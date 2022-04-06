from bottle import  get, view, request, redirect, post, template
import g
import mysql

@get("/mytweets")
@view("mytweets")
def _():
    try:
###################### DEFINING THE VARIABLES ########################
        error = request.forms.get("error")
        user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
        user_first_name = request.get_cookie("user_first_name", secret=g.COOKIE_SECRET)
        user_last_name = request.get_cookie("user_last_name", secret=g.COOKIE_SECRET)
        user_session_id = request.get_cookie("uuid4")
        tweet_description = request.forms.get("tweet_description")
        tweet_title = request.forms.get("tweet_title")
        image_tweet = request.files.get("image_tweet")





###################### CONNECTING TO THE DATABASE ########################
        db_config = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)

        

        sql = """SELECT * FROM tweets  WHERE tweet_user_email =%s """
        cursor.execute(sql, (user_email,))
        tweets = cursor.fetchall() 
        print("All the tweets are listed")

        sql_sessions=""" SELECT * FROM sessions WHERE session_id =%s"""
        cursor.execute(sql_sessions, (user_session_id,))
        session = cursor.fetchone()
        print(session)


        db.commit()

    except Exception as ex:
        print(ex)
    finally:
        db.close()

###################### RETURN - DICTIONARY ########################
    if session is None:
        return redirect("/login")
    
        
    return dict( error = error, tweet_description=tweet_description, 
                    user_first_name=user_first_name, user_last_name=user_last_name, 
                    tweet_title=tweet_title, user_email=user_email, tweets = tweets, image_tweet = image_tweet)
