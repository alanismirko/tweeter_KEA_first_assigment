from bottle import get, view, request, route
import g
import mysql

@get("/user_profile/<user_profile_email>")
@view("user_profile")
def _(user_profile_email):
    try:
        user_profile_email = request.params.get("user_profile_email")
        user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
        error = request.params.get("error")
        tweet_description = request.params.get("tweet_description")
        tweet_title = request.params.get("tweet_title")
        print(user_profile_email)



        db_config = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)

        

        sql = """SELECT * FROM users  WHERE user_email =%s """
        cursor.execute(sql, (user_profile_email,))
        users = cursor.fetchall() 
        print(users)

        

    except Exception as ex:
        print(ex)
    finally:
        db.close()

        return dict( error = error, tweet_description=tweet_description, 
                    tweet_title=tweet_title, user_email=user_email, users=users, user_profile_email= user_profile_email)