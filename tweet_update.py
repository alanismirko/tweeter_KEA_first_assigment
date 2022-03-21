from bottle import post, request, redirect, get, view
import g
import uuid
import time
from datetime import datetime
import mysql.connector

@post("/tweet_update/<tweet_id_update>")
@view("index")
def _(tweet_id_update):
    
    try:
###################### VARIABLES #######################################
        
        user_session_id = request.get_cookie("uuid4")
        tweet_user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)

        tweet_id_update = request.forms.get("tweet_id_update")
        tweet_title_update = request.forms.get("tweet_title_update")
        tweet_description_update = request.forms.get("tweet_description_update")
        tweet_created_at_update = request.forms.get("tweet_created_at_update")
        tweet_updated_at_update = request.forms.get("tweet_updated_at_update")

        tweet ={
            "tweet_id": tweet_id_update,
            "tweet_title": tweet_title_update,
            "tweet_description": tweet_description_update,
            "tweet_created_at": tweet_created_at_update,
            "tweet_updated_at": tweet_updated_at_update,
            "tweet_user_email": tweet_user_email
        }

###################### CONNECTING TO THE DATABASE ########################
        db_config = {
            "host": "localhost",
            "user":"root",
            "database": "tweeterdb",
            "password": "1234"
            }

        db = mysql.connector.connect(**db_config)
            
        cursor = db.cursor(buffered=True)
        sql = """ UPDATE  tweets 
                SET tweet_description =%s,
                tweet_title =%s,
                tweet_created_at =%s,
                tweet_updated_at =%s,
                tweet_user_email =%s
        WHERE tweet_id=%s"""
        var = (tweet_description_update, tweet_title_update, tweet_created_at_update, tweet_updated_at_update, tweet_user_email, tweet_id_update,)
        cursor.execute(sql, var)
        db.commit()
        print("tweet is deleted", tweet_id_update)

    except Exception as ex:
        print(ex)
    finally:
        db.close()

    return redirect("/index")



