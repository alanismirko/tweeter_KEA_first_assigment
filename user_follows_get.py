from bottle import view, get, request, response
import g
import mysql

@get("/following")
@view("user_follows")
def _():
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    error = request.params.get("error")
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")
    tabs = g.TABS

    try:
        # import production
        # db_config = g.PRODUCTION_CONN
        db_config = g.DEVELOPMENT_CONN

    except Exception as ex:
        print(ex)

    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)
    
        sql = """SELECT * FROM follows WHERE user_email_initiator = %s"""
        val = (user_email, )
        cursor.execute(sql, val)
        follows = cursor.fetchall()

        sql = """SELECT * FROM users  WHERE user_email =%s """
        cursor.execute(sql, (user_email,))
        users = cursor.fetchall() 
        db.commit()
    except Exception as ex:
        print(ex)
        response.status = 500

    finally:
        db.close()

    return dict(users= users, user_email = user_email, error=error, tweet_description=tweet_description,follows=follows, tweet_title=tweet_title, tabs=tabs)
