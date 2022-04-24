from bottle import post, request, redirect, get, view
import g
import uuid
import time
from datetime import datetime
import mysql.connector

@get("/logout")
def _():
###################### VARIABLES #######################################
        
    user_session_id = request.get_cookie("uuid4")

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
        sql = """ DELETE FROM sessions WHERE session_id=%s"""

        cursor.execute(sql, (user_session_id,))
        print("session is deleted", user_session_id )
        db.commit()
    except Exception as ex:
        print(ex)
    finally:
        db.close()

###################### RETURN ########################
    return redirect("/login")




