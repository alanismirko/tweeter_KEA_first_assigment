from bottle import post, request, redirect, get, view, response
import g
import uuid
import time
from datetime import datetime
import mysql.connector
import os

@post("/delete_tweet/<tweet_id_update>")
@view("/mytweets")
def _(tweet_id_update):
    
###################### VARIABLES #######################################
        
    user_session_id = request.get_cookie("uuid4")
    tweet_id_update = request.forms.get("tweet_id_update")
    image_id = request.forms.get("image_id")


###################### CONNECTING TO THE DATABASE ########################
    try:
        import production
        db_config = g.PRODUCTION_CONN

    except Exception as ex:
        print(ex)
        db_config = g.DEVELOPMENT_CONN

    try:

        db = mysql.connector.connect(**db_config)
            
        cursor = db.cursor(buffered=True)
        db.autocommit = False

        sql = """ DELETE FROM tweets WHERE tweet_id=%s"""
        cursor.execute(sql, (tweet_id_update,))
        print("tweet is deleted", tweet_id_update)

        sql_sessions=""" SELECT * FROM sessions WHERE session_id =%s"""
        cursor.execute(sql_sessions, (user_session_id,))
        session = cursor.fetchone()
        print(session)

        cursor.callproc('DeleteSession')

        if  image_id is not None:
            os.remove(f"images/{image_id}")

        db.commit()

    except Exception as ex:
        print(ex)
        db.rollback()
    finally:
        db.close()

    if session is None:
            return redirect("/login")
    return redirect("/myprofile")



###################### DELETE ADMIN ########################

@post("/delete_tweet_admin/<tweet_id_update>")
def _(tweet_id_update):
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")

###################### DEFINING THE VARIABLES ########################
    error = request.params.get("error")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    user_email_admin = request.forms.get("user_email")
    user_first_name = request.get_cookie("user_first_name", secret=g.COOKIE_SECRET)
    user_last_name = request.get_cookie("user_last_name", secret=g.COOKIE_SECRET)
    user_session_id = request.get_cookie("uuid4")
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")
    image_tweet = request.files.get("image_tweet")
    tweet_id_update = request.forms.get("tweet_id_update")

###################### CONNECTING TO THE DATABASE ########################
    try:
        import production
        db_config = g.PRODUCTION_CONN

    except Exception as ex:
        print(ex)
        db_config = g.DEVELOPMENT_CONN


    try:

        db = mysql.connector.connect(**db_config)
        db.autocommit = False
        cursor = db.cursor(buffered=True)

        
        sql = """SELECT * FROM tweets  """
        cursor.execute(sql,)
        tweets = cursor.fetchall() 

        sql_sessions=""" SELECT * FROM sessions WHERE session_id =%s"""
        cursor.execute(sql_sessions, (user_session_id,))
        session = cursor.fetchone()
        print(session)

        sql = """ DELETE FROM tweets WHERE tweet_id=%s"""
        cursor.execute(sql, (tweet_id_update,))
        print("tweet is deleted", tweet_id_update)

        
        sql = """DELETE FROM sessions WHERE TIMESTAMPDIFF(MINUTE,session_created_at,NOW()) > 30; """
        cursor.execute(sql)
        print("User session is deleted")
        db.commit()
        response.status = 200

    except Exception as ex:
        print(ex)
        db.rollback()
        response.status = 500

    finally:
        db.close()

###################### RETURN  ########################
    if session is None:
        return redirect(f"/login")
    return redirect(f"/admin")



