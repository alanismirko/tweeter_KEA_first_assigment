from bottle import get, view, request, response
import g
import mysql

@get("/myprofile")
@view("myprofile")
def _():
    error = request.params.get("error")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    user_session_id = request.get_cookie("uuid4")
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")

    try:
        # import production
        # db_config = g.PRODUCTION_CONN
        db_config = g.DEVELOPMENT_CONN

    except Exception as ex:
        print(ex)

    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)

        sql = """SELECT * FROM users  WHERE user_email =%s """
        cursor.execute(sql, (user_email,))
        users = cursor.fetchall() 
        print(users)

        db.commit()
    except Exception as ex:
        print(ex)
        response.status = 500

    finally:
        db.close()


    return dict( error = error, tweet_description=tweet_description, 
                    tweet_title=tweet_title, user_email=user_email, users=users)
