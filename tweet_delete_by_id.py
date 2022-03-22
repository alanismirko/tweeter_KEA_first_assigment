from bottle import post, request, redirect, get, view
import g
import uuid
import time
from datetime import datetime
import mysql.connector

@post("/delete_tweet/<tweet_id_update>")
@view("index")
def _(tweet_id_update):
    
    try:
###################### VARIABLES #######################################
        
        user_session_id = request.get_cookie("uuid4")
        tweet_id_update = request.forms.get("tweet_id_update")

###################### CONNECTING TO THE DATABASE ########################
        db_config = {
            "host": "localhost",
            "user":"root",
            "database": "tweeterdb",
            "password": "1234"
            }

        db = mysql.connector.connect(**db_config)
            
        cursor = db.cursor(buffered=True)
        sql = """ DELETE FROM tweets WHERE tweet_id=%s"""

        cursor.execute(sql, (tweet_id_update,))
        db.commit()
        print("tweet is deleted", tweet_id_update)

    except Exception as ex:
        print(ex)
    finally:
        db.close()

###################### RETURN ########################

    if user_session_id not in g.SESSIONS:
            return redirect("/login")
    else:
        return redirect("/index")



