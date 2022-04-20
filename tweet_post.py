from bottle import post, request, redirect, get, view, template, response
import g
import uuid
import time
from datetime import datetime
import mysql.connector
import os
import imghdr


@post("/create_tweet")
def _():

    ###################### VARIABLES #######################################
    tweet_id = str(uuid.uuid4())
    tweet_title = request.forms.get("tweet_title")
    tweet_description = request.forms.get("tweet_description")
    user_session_id = request.get_cookie("uuid4")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    tweet_created_at = str(int(time.time()))
    image_id = str(uuid.uuid4())
    image_tweet = request.files.get("image_tweet")
    if  image_tweet is not None:
        file_extension = os.path.splitext(image_tweet.filename)
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
    if image_tweet is None:
        image_name = "No image added"

    if len(tweet_title) < 2 or len(tweet_title) > 100:
        response.status = 400
        return redirect(f"/index?error=tweet_title&tweet_title={tweet_title}&tweet_description={tweet_description}")
    if len(tweet_description) < 2 or len(tweet_description)>100:
        response.status = 400
        return redirect(f"/index?error=tweet_description&tweet_title={tweet_title}&tweet_description={tweet_description}")

    try:
###################### CONNECTING TO THE DATABASE ########################
        db_config = {
            "host": "localhost",
            "user":"root",
            "database": "tweeterdb",
            "password": "1234"
            }

        db = mysql.connector.connect(**db_config)
            
        cursor = db.cursor()

        sql = """SELECT * FROM sessions  WHERE session_id =%s """
        cursor.execute(sql, (user_session_id,))
        session = cursor.fetchone() 

        sql = """INSERT INTO tweets (tweet_id, tweet_description, tweet_title, tweet_created_at, tweet_user_email, tweet_image_id ) VALUES (%s, %s, %s, %s, %s, %s)"""
        val = (tweet_id,tweet_description,tweet_title, tweet_created_at, user_email, image_name,)
        cursor.execute(sql, val)
        print("tweet is created")


        
        db.commit()

    except Exception as ex:
        print(ex)
    finally:
        db.close()
    
    if session is None:
        return redirect("/login")



