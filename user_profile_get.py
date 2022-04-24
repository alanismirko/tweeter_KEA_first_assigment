from bottle import get, view, request, route, redirect
import g
import mysql

@get("/user_profile")
@view("user_profile")
def _():
    user_profile_email = request.params.get("user_profile_email")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    error = request.params.get("error")
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")

    try:
        import production
        db_config = g.PRODUCTION_CONN
    except Exception as ex:
        print(ex)
        db_config = g.DEVELOPMENT_CONN
    try:

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)

        

        sql = """SELECT * FROM users  WHERE user_email =%s """
        cursor.execute(sql, (user_profile_email,))
        users = cursor.fetchall() 

        sql = """SELECT * FROM tweets  WHERE tweet_user_email =%s """
        cursor.execute(sql, (user_profile_email,))
        tweets = cursor.fetchall() 
        print("All the tweets are listed")

        db.commit()

    except Exception as ex:
        print(ex)

    finally:
        db.close()

    if user_email == user_profile_email:
            return redirect("/myprofile")

    return dict( error = error, tweet_description=tweet_description, 
                    tweet_title=tweet_title, user_email=user_email, users=users, user_profile_email= user_profile_email, tweets=tweets)





