from bottle import view, get, request
import g
import mysql

@get("/following")
@view("user_following")
def _():
    try:
        user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
        error = request.params.get("error")
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
    
        sql = """SELECT * FROM FOLLOWS WHERE user_email_initiator = %s"""
        val = (user_email, )
        
        cursor.execute(sql, val)

        follows = cursor.fetchall()

    except Exception as ex:
        print(ex)
    finally:
        db.close()

    return dict(user_email = user_email, error=error, tweet_description=tweet_description,follows=follows, tweet_title=tweet_title)


@get("/followers")
@view("user_followers")
def _():
    try:
        user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
        error = request.params.get("error")
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
    
        sql = """SELECT * FROM FOLLOWS WHERE user_email_receiver = %s"""
        val = (user_email, )
        
        cursor.execute(sql, val)

        follows = cursor.fetchall()
        db.commit()

    except Exception as ex:
        print(ex)
    finally:
        db.close()

    return dict(user_email = user_email, error=error, tweet_description=tweet_description,follows=follows, tweet_title=tweet_title)