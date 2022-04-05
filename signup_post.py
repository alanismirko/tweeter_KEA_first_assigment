from bottle import  post, request, redirect
import g
import re
import uuid
import time
from datetime import datetime
import mysql.connector
import bcrypt


@post("/signup")
def _():
    try:

############### DEFINING THE USER, ADDRESS AND ZIPCODE #######################################
        user_id = str(uuid.uuid4())
        user_first_name = request.forms.get("user_first_name")
        user_last_name = request.forms.get("user_last_name")
        user_email = request.forms.get("user_email")
        street_name = request.params.get("street_name")
        street_number = request.params.get("street_number")
        country = request.params.get("country")
        region = request.params.get("region")
        zipcode = request.params.get("zipcode")
        city = request.params.get("city")
        user_address_id = str(uuid.uuid4())

        user_password = request.forms.get("user_password").encode("utf-8")
        salt = bcrypt.gensalt()
        password_hashed = bcrypt.hashpw(user_password, salt)
        user_created_at = str(int(time.time()))
    

############### VALIDATION #######################################

        if not request.forms.get("user_email"):
            return redirect(f"/signup?error=user_email&user_first_name={user_first_name}&user_last_name={user_last_name}&street_name={street_name}&street_number={street_number}&country={country}&region={region}&zipcode={zipcode}&city={city}")
        if not re.match(g.REGEX_EMAIL,user_email):
            return redirect(f"/signup?error=user_email&user_first_name={user_first_name}&user_last_name={user_last_name}&street_name={street_name}&street_number={street_number}&country={country}&region={region}&zipcode={zipcode}&city={city}")

        if not user_password:
            return redirect(f"/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}&street_name={street_name}&street_number={street_number}&country={country}&region={region}&zipcode={zipcode}&city={city}")
        if len(user_password) < 6:
            return redirect(f"/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}&street_name={street_name}&street_number={street_number}&country={country}&region={region}&zipcode={zipcode}&city={city}")
        if len(user_password) > 50:
            return redirect(f"/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}&street_name={street_name}&street_number={street_number}&country={country}&region={region}&zipcode={zipcode}&city={city}")

        if len(user_first_name) < 2:
            return redirect(f"/signup?error=user_first_name&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}&street_name={street_name}&street_number={street_number}&country={country}&region={region}&zipcode={zipcode}&city={city}")
        if len(user_last_name) < 2:
            return redirect(f"/signup?error=user_last_name&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}&street_name={street_name}&street_number={street_number}&country={country}&region={region}&zipcode={zipcode}&city={city}")


############### DB CONNECTION AND TRSANSACTION #####################

        db_config = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }


        db = mysql.connector.connect(**db_config)
        db.autocommit = False
        cursor = db.cursor()

        sql = """INSERT INTO zipcodes (zipcode,city) VALUES (%s, %s)"""
        val = (zipcode, city )
        cursor.execute(sql, val)

        sql = """INSERT INTO addresses (address_id,street_name,street_number, country, region, zipcode) VALUES (%s,%s, %s, %s, %s, %s)"""
        val = (user_address_id,street_name,street_number,country, region, zipcode, )
        cursor.execute(sql, val)

        sql = """INSERT INTO users (user_id, user_first_name, user_last_name, user_email, user_password, user_created_at, user_address_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        val = (user_id,user_first_name,user_last_name, user_email, password_hashed, user_created_at, user_address_id, )
        cursor.execute(sql, val)

        db.commit()
        
    except Exception as ex:
        print(ex)
        db.rollback()
    finally:
        db.close()
    return redirect("/login")



