from bottle import get, view, request, route, redirect, post
import g
import mysql

@post("/like")
def _():
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    tweet_id_update = request.forms.get("tweet_id_update")

    try:
        db_config = g.PRODUCTION_CONN
    except Exception as ex:
        print("ex")
        db_config = g.DEVELOPMENT_CONN

    try:
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
    finally:
        db.close()
    return redirect("/index")

