from bottle import request, redirect, post, response
import g 
import re
import uuid
import jwt
import mysql.connector


@post("/login")
def _login():

    try:
###################### VARIABLES #######################################
        user_email = request.forms.get("user_email")
        user_password = request.forms.get("user_password")
        user_session_id = str(uuid.uuid4())
        encoded_jwt = jwt.encode({"uuid4": user_session_id, "user_email":user_email}, "secret key", algorithm="HS256")

###################### SETTING THE COOKIE ##############################

        response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)
        response.set_cookie("encoded_jwt", encoded_jwt)
        response.set_cookie("uuid4", user_session_id)

        g.SESSIONS.append(user_session_id)

###################### CONNECTING TO THE DATABASE ########################

        db_config = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        sql = """SELECT * FROM users WHERE user_email =%s AND user_password=%s """
        var = (user_email, user_password)
        cursor.execute(sql, var)
        user = cursor.fetchone()
        db.commit()
        
    except Exception as ex:
        print(ex)
    finally:
        db.close()

###################### RETURN ########################
    if not user: 
            return redirect(f"/login?error=wrong_credentials") 
    else:
        return redirect(f"/index")  
    
    