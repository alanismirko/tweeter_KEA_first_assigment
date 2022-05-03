from bottle import request, redirect, post, response
import g 
import re
import uuid
import jwt
import mysql.connector
import time
from datetime import datetime
import bcrypt
import mysql


@post("/login")
def _():
###################### VARIABLES #######################################
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")

    user_email = request.forms.get("user_email")
    user_session_id = str(uuid.uuid4())
    encoded_jwt = jwt.encode({"uuid4": user_session_id, "user_email":user_email}, "secret key", algorithm="HS256")
    session_created_at = ""
    user_password_admin = request.forms.get("user_password")

    user_password = request.forms.get("user_password").encode("utf-8")
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.checkpw(user_password, salt)

###################### SETTING THE COOKIE ##############################

    response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)
    response.set_cookie("encoded_jwt", encoded_jwt)
    response.set_cookie("uuid4", user_session_id)
    response.set_cookie("session_created_at", session_created_at)

###################### CONNECTING TO THE DATABASE ########################
    try:
        import production
        db_config = g.PRODUCTION_CONN

    except Exception as ex:
        print(ex)
        db_config = g.DEVELOPMENT_CONN




    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        sql_login = """SELECT * FROM users WHERE user_email =%s AND user_password=%s """
        var = (user_email, password_hashed)
        cursor.execute(sql_login, var)
        users = cursor.fetchone()
        print("User is logged in")

        sql_session= """ INSERT INTO sessions (session_id, session_user_email) VALUES (%s,%s)  """
        val_session = (user_session_id, user_email, )
        cursor.execute(sql_session, val_session)
        print("Session is added")

        db.commit()
        response.status = 200

    except Exception as ex:
        response.status= 500
        print(ex)

    finally:
        db.close()

###################### RETURN ########################
    if not users: 
            return redirect(f"/login?error=wrong_credentials") 
    if user_email == "admin@gmail.com" and user_password_admin=="admin":
        return redirect("/admin")
    else:
        return redirect("/index")  
    
    