from bottle import post, request, redirect, get, view, response
import g
import uuid
import time
from datetime import datetime
import mysql.connector

@post("/tweet_update/<tweet_id_update>")
def _(tweet_id_update):

    user_session_id = request.get_cookie("uuid4")
    tweet_user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)

    tweet_id_update = request.forms.get("tweet_id_update")
    tweet_title_update = request.forms.get("tweet_title_update")
    tweet_description_update = request.forms.get("tweet_description_update")
    tweet_created_at_update = request.forms.get("tweet_created_at_update")
    tweet_updated_at_update = request.forms.get("tweet_updated_at_update")

    if len(tweet_title_update) < 2 or len(tweet_title_update) > 100:
        response.status = 400
        return redirect(f"/index?error=tweet_title&tweet_title={tweet_title_update}&tweet_description={tweet_description_update}")
    if len(tweet_description_update) < 2 or len(tweet_description_update)>100:
        response.status = 400
        return redirect(f"/index?error=tweet_description&tweet_title={tweet_title_update}&tweet_description={tweet_description_update}")

###################### CONNECTING TO THE DATABASE ########################
    try:
        # import production
        # db_config = g.PRODUCTION_CONN
        db_config = g.DEVELOPMENT_CONN

    except Exception as ex:
        print(ex)

    try:
        db = mysql.connector.connect(**db_config)
        db.autocommit = False          
        cursor = db.cursor(buffered=True)

        sql = """ UPDATE  tweets 
                SET tweet_description =%s,
                tweet_title =%s,
                tweet_created_at =%s,
                tweet_user_email =%s
        WHERE tweet_id=%s"""

        var = (tweet_description_update, tweet_title_update, tweet_created_at_update, tweet_user_email, tweet_id_update,)
        cursor.execute(sql, var)

        sql = """SELECT * FROM sessions  WHERE session_id =%s """
        cursor.execute(sql, (user_session_id,))
        session = cursor.fetchone() 

        sql = """DELETE FROM sessions WHERE TIMESTAMPDIFF(MINUTE,session_created_at,NOW()) > 30; """
        cursor.execute(sql)

        db.commit()

    except Exception as ex:
        print(ex)
        db.rollback()
        response.status = 500


    finally:
        db.close()

###################### RETURN ########################
    if session is None:
            return redirect("/login")
    else:
        return redirect("/mytweets")



