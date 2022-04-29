from bottle import get, view, request, response
import g
import mysql

@get("/myprofile")
@view("myprofile")
def _():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")

    error = request.params.get("error")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    user_session_id = request.get_cookie("uuid4")
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")

    tabs = g.TABS
    trends = g.TRENDS
    reccomendations = g.RECOMMENDATIONS

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
        cursor.execute(sql, (user_email,))
        users = cursor.fetchall() 
        print(users)

        sql = """SELECT * FROM tweets  WHERE tweet_user_email =%s """
        cursor.execute(sql, (user_email,))
        tweets = cursor.fetchall() 
        print("All the tweets are listed")

        sql = """DELETE FROM sessions WHERE TIMESTAMPDIFF(MINUTE,session_created_at,NOW()) > 30; """
        cursor.execute(sql)
        print("User session is deleted")

        db.commit()
    except Exception as ex:
        print(ex)
        response.status = 500

    finally:
        db.close()


    return dict( error = error, tweet_description=tweet_description, tweet_title=tweet_title, user_email=user_email, users=users, tabs=tabs, tweets= tweets, trends=trends, reccomendations=reccomendations)
