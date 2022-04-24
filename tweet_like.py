from bottle import get, view, request, route, redirect, post
import g
import mysql

@post("/like")
def _():
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    tweet_id_update = request.forms.get("tweet_id_update")

    try:
        import production
        db_config = {
                "host":"keatest2020web.mysql.eu.pythonanywhere-services.com",
                "user": "keatest2020web",
                "password": "MySqLpassword",
                "database": "keatest2020web$tweeterdb",
        }

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)


        sql = """INSERT INTO tweets_liked (tweet_id, user_email ) VALUES (%s, %s)"""
        val = (tweet_id_update, user_email,)
        cursor.execute(sql,val)

        sql =""" SELECT COUNT(*) FROM tweets_liked WHERE tweet_id=%s """
        cursor.execute(sql, tweet_id_update,)
        all = cursor.fetchall()
        print("the count is", all)
        db.commit()

    except Exception as ex:
        print(ex)

        db_config = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)


        sql = """INSERT INTO tweets_liked (tweet_id, user_email ) VALUES (%s, %s)"""
        val = (tweet_id_update, user_email,)
        cursor.execute(sql,val)

        sql =""" SELECT COUNT(*) FROM tweets_liked WHERE tweet_id=%s """
        cursor.execute(sql, tweet_id_update,)
        all = cursor.fetchall()
        print("the count is", all)
        db.commit()


    finally:
        db.close()
    return redirect("/index")

