from bottle import post, request, redirect, get, view, template
import g
import uuid
import time
from datetime import datetime
import mysql.connector
import os
import imghdr

@post("/create_tweet")
@view("index")
@view("mytweets")
def _():
    
    try:
###################### VARIABLES #######################################
        tweet_id = str(uuid.uuid4())
        tweet_title = request.forms.get("tweet_title")
        tweet_description = request.forms.get("tweet_description")
        user_session_id = request.get_cookie("uuid4")
        user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
        tweet_created_at = str(int(time.time()))
        tweet_updated_at = ""
        error = request.params.get("error")
        image_id = str(uuid.uuid4())
        image_tweet = request.files.get("image_tweet")
        file_name, file_extension = os.path.splitext(image_tweet.filename)

        tweet = {
            "tweet_id": tweet_id, 
            "tweet_title": tweet_title, 
            "tweet_description":tweet_description,
            "tweet_created_at": tweet_created_at,
            "tweet_updated_at": tweet_updated_at,
            "tweet_user_email": user_email
            }


###################### VALIDATION #######################################
        if len(tweet_title) < 1:
            return redirect(f"index?error=tweet_title_create&tweet_description={tweet_description}&tweet_title={tweet_title}")
        if len(tweet_description) < 1:
            return redirect(f"index?error=tweet_description_create&tweet_title={tweet_title}&tweet_description={tweet_description}")

###################### IMAGE VALIDATION AND SAVING #######################################

        if file_extension not in (".png", ".jpeg", ".jpg"):
            return "image not allowed"
        if file_extension == ".jpg": file_extension = ".jpeg"

        image_name =f"{image_id}{file_extension}"
        image_tweet.save(f"images/{image_name}")

        imghdr_extension = imghdr.what(f"images/{image_name}")
        if file_extension != f".{imghdr_extension}":
            print("not an image")
            os.remove(f"images/{image_name}")
            return "removing the suspicious file..."
###################### CONNECTING TO THE DATABASE ########################
        db_config = {
            "host": "localhost",
            "user":"root",
            "database": "tweeterdb",
            "password": "1234"
            }

        db = mysql.connector.connect(**db_config)
            
        cursor = db.cursor()
        sql = """INSERT INTO tweets (tweet_id, tweet_description, tweet_title, tweet_created_at, tweet_user_email, tweet_image_id ) VALUES (%s, %s, %s, %s, %s, %s)"""
        val = (tweet_id,tweet_description,tweet_title, tweet_created_at, user_email, image_name,)
        
        cursor.execute(sql, val)
        print("tweet is created", tweet)

        sql = """SELECT * FROM sessions  WHERE session_id =%s """
        cursor.execute(sql, (user_session_id,))
        session = cursor.fetchone() 

        sql = """SELECT * FROM tweets  WHERE tweet_user_email =%s """
        cursor.execute(sql, (user_email,))
        tweets = cursor.fetchall() 
        print("All the tweets are listed")
        
        db.commit()


        print("All the tweets are listed")

    except Exception as ex:
        print(ex)
    finally:
        db.close()

###################### RETURN ########################
    if session is None:
            return redirect("/login")
    return dict(error=error, user_email=user_email,tweet_title=tweet_title, tweet_description=tweet_description, tweets=tweets, image_name = image_name)


