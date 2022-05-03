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
        db.autocommit = False          
        cursor = db.cursor()

        sql = """INSERT INTO tweets_liked (tweet_id, user_email ) VALUES (%s, %s)"""
        val = (tweet_id_update, user_email,)
        cursor.execute(sql,val)
        all = cursor.fetchall()
        print()

        sql = """UPDATE tweets
                SET tweet_like_count = tweet_like_count + 1
                WHERE tweet_id = %s"""
        cursor.execute(sql, (tweet_id_update,))

        db.commit()

        response.status = 200

    except Exception as ex:
        print(ex)
        db.rollback()

        response.status = 500

    finally:
        db.close()
    
    return redirect("/index")





