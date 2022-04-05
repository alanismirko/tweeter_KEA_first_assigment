from bottle import post, request, redirect, get, view
import g
import uuid
import time
from datetime import datetime
import mysql.connector

@post("/search_tweet")
@view("/index")
def _():
    
    try:
###################### VARIABLES #######################################
        
        search_term = request.forms.get("search_term")
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
        sql = """ SELECT * FROM users WHERE MATCH(user_email)
                AGAINST('search_term' IN BOOLEAN MODE)"""

        cursor.execute(sql, (search_term,))
        print("result", search_term)

        sql_sessions=""" SELECT * FROM sessions WHERE session_id =%s"""
        cursor.execute(sql_sessions, (user_session_id,))
        session = cursor.fetchone()
        print(session)

        db.commit()


    except Exception as ex:
        print(ex)
    finally:
        db.close()

###################### RETURN ########################
    if session is None:
            return redirect("/login")


    return redirect("/mytweets")



