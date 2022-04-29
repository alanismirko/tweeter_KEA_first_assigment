from bottle import get, view, request, route, redirect, post, response
import g
import mysql

@post("/like/<tweet_id_update>")
def _(tweet_id_update):
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")

    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    tweet_id_update = request.forms.get("tweet_id_update")

    try:
        import production
        db_config = g.PRODUCTION_CONN

    except Exception as ex:
        print(ex)
        db_config = g.DEVELOPMENT_CONN


    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)


        sql = """INSERT INTO tweets_liked (tweet_id, user_email ) VALUES (%s, %s)"""
        val = (tweet_id_update, user_email,)
        cursor.execute(sql,val)

        sql =""" SELECT COUNT(*) FROM tweets_liked WHERE tweet_id=%s """
        cursor.execute(sql, (tweet_id_update,))
        all = cursor.fetchall()
        print("the count is", all, "tweet id", tweet_id_update)

        db.commit()


    except Exception as ex:
        print(ex)
        response.status = 500

    finally:
        db.close()


