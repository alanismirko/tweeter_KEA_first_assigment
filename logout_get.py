from bottle import post, request, redirect, get, view
import g
import uuid
import time
from datetime import datetime
import mysql.connector

@get("/logout")
def _():
    try:
###################### VARIABLES #######################################
        
        user_session_id = request.get_cookie("uuid4")

###################### CONNECTING TO THE DATABASE ########################
        db_config = {
            "host": "localhost",
            "user":"root",
            "database": "tweeterdb",
            "password": "1234"
            }

        db = mysql.connector.connect(**db_config)
            
        cursor = db.cursor(buffered=True)
        sql = """ DELETE FROM sessions WHERE session_id=%s"""

        cursor.execute(sql, (user_session_id,))
        db.commit()
        print("session is deleted", user_session_id )


    except Exception as ex:
        print(ex)
    finally:
        db.close()

###################### RETURN ########################
    return redirect("/login")




