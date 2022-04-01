from bottle import request, redirect, post, response
import g 
import re
import uuid
import jwt
import mysql.connector
import time
from datetime import datetime


@post("/login")
def _login():

    try:
###################### VARIABLES #######################################
        user_email = request.forms.get("user_email")
        user_password = request.forms.get("user_password")
        user_session_id = str(uuid.uuid4())
        encoded_jwt = jwt.encode({"uuid4": user_session_id, "user_email":user_email}, "secret key", algorithm="HS256")
        user_created_at = str(int(time.time()))


###################### SETTING THE COOKIE ##############################

        response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)
        response.set_cookie("encoded_jwt", encoded_jwt)
        response.set_cookie("uuid4", user_session_id)


###################### CONNECTING TO THE DATABASE AND TRANSACTIONS ########################

        db_config = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        sql_login = """SELECT * FROM users WHERE user_email =%s AND user_password=%s """
        var = (user_email, user_password)
        cursor.execute(sql_login, var)
        user = cursor.fetchone()
        print("User is logged in")

        sql_session= """ INSERT INTO sessions (session_id, session_user_email, session_created_at) VALUES (%s,%s,%s)  """
        val_session = (user_session_id, user_email,user_created_at )
        cursor.execute(sql_session, val_session)
        print("Session is added")

        db.commit()
        
    except Exception as ex:
        print(ex)
        db.rollback()
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            print("connnection is closed")

###################### RETURN ########################
    if not user: 
            return redirect(f"/login?error=wrong_credentials") 
    else:
        return redirect(f"/index")  
    
    