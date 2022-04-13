from bottle import get, view, request
import g
import mysql

@get("/myprofile")
@view("myprofile")
def _():
    try:
        error = request.params.get("error")
        user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
        user_session_id = request.get_cookie("uuid4")
        tweet_description = request.params.get("tweet_description")
        tweet_title = request.params.get("tweet_title")


        db_config = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)

        

        sql = """SELECT * FROM users  WHERE user_email =%s """
        cursor.execute(sql, (user_email,))
        users = cursor.fetchall() 
        print(users)

        

    except Exception as ex:
        print(ex)
    finally:


        return dict( error = error, tweet_description=tweet_description, 
                    tweet_title=tweet_title, user_email=user_email, users=users)
