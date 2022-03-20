from bottle import  post, request, redirect
import g
import re
import uuid
import time
from datetime import datetime
import mysql.connector


@post("/signup")
def _():
    try:

############### DEFINING THE USER #######################################
        user_id = str(uuid.uuid4())
        user_first_name = request.forms.get("user_first_name")
        user_last_name = request.forms.get("user_last_name")
        user_email = request.forms.get("user_email")
        user_password = request.forms.get("user_password")
        user_created_at = str(int(time.time()))

        user = {
            "user_id":user_id,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_email": user_email,
            "user_password": user_password,
            "user_created_at": user_created_at,
            "user_updated_at": user_updated_at
        }


############### VALIDATION #######################################

        if not request.forms.get("user_email"):
            return redirect(f"/signup?error=user_email&user_first_name={user_first_name}&user_last_name={user_last_name}")
        if not re.match(g.REGEX_EMAIL,user_email):
            return redirect(f"/signup?error=user_email&user_first_name={user_first_name}&user_last_name={user_last_name}")

        if not user_password:
            return redirect(f"/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
        if len(user_password) < 6:
            return redirect(f"/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
        if len(user_password) > 50:
            return redirect(f"/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")

        if len(user_first_name) < 2:
            return redirect(f"/signup?error=user_first_name&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
        if len(user_last_name) < 2:
            return redirect(f"/signup?error=user_last_name&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
    
############### DB CONNECTION AND EXECUTION #####################

        db_config = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        sql = """INSERT INTO users (user_id, user_first_name, user_last_name, user_email, user_password, user_created_at) VALUES (%s, %s, %s, %s, %s, %s)"""
        val = (user_id,user_first_name,user_last_name, user_email, user_password, user_created_at)
        
        cursor.execute(sql, val)
        db.commit()
        print("user is created", user)
        
    except Exception as ex:
        print(ex)
    finally:
        db.close()


    return redirect("/login")
