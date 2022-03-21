from bottle import  get, view, request, redirect
import g
import mysql.connector




@get("/index")
@view("index")
def _():
    try:
        error = request.forms.get("error")
        user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
        user_first_name = request.get_cookie("user_first_name", secret=g.COOKIE_SECRET)
        user_last_name = request.get_cookie("user_last_name", secret=g.COOKIE_SECRET)
        user_session_id = request.get_cookie("uuid4")
        tweet_description = request.forms.get("tweet_description")
        tweet_title = request.forms.get("tweet_title")

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
        db.commit()
        print("Inserted",cursor.rowcount,"row(s) of data.")


    except Exception as ex:
        print(ex)
    finally:
        db.close()
    return dict( error = error, tweet_description=tweet_description, 
                    user_first_name=user_first_name, user_last_name=user_last_name, 
                    tweet_title=tweet_title, user_email=user_email, tweets = tweets)
        