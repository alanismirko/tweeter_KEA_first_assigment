from bottle import post, request, redirect, get, view
import g
import uuid
import time
from datetime import datetime
import mysql.connector

@post("/create_tweet")
def _():
    try:
###################### VARIABLES #######################################
        tweet_id = str(uuid.uuid4())
        tweet_title = request.forms.get("tweet_title")
        tweet_description = request.forms.get("tweet_description")
        tweet_id = request.forms.get("tweet_description")
        user_session_id = request.get_cookie("uuid4")
        user_session_email = request.get_cookie("user_email")
        tweet_created_at = str(int(time.time()))
        tweet_updated_at = ""


        tweet = {
            "tweet_id": tweet_id, 
            "tweet_title": tweet_title, 
            "tweet_description":tweet_description,
            "tweet_created_at": tweet_created_at,
            "tweet_updated_at": tweet_updated_at
            }


###################### VALIDATION #######################################
        if len(tweet_title) < 1:
            return redirect(f"tweets?error=tweet_title_create&tweet_description={tweet_description}&tweet_title={tweet_title}")
        if len(tweet_description) < 1:
            return redirect(f"tweets?error=tweet_description_create&tweet_title={tweet_title}&tweet_description={tweet_description}")

###################### USER LOGGED IN #######################################
        if user_session_id not in g.SESSIONS:
            return redirect("/login")

###################### CONNECTING TO THE DATABASE ########################
        db_config = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        sql = """INSERT INTO tweets (tweet_id, tweet_description, tweet_title, tweet_created_at, tweet_updated_at) VALUES (%s, %s, %s, %s, %s) WHERE tweet_user_email = %s"""
        val = (tweet_id,tweet_description,tweet_title, tweet_created_at, tweet_updated_at, user_session_email)
        
        cursor.execute(sql, val)
        db.commit()
        print("tweet is created", tweet)

    except Exception as ex:
        print(ex)
    finally:
        db.close()

    return redirect("/index")



