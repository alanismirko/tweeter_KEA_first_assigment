from bottle import  post, request, redirect, get
import g
import re
import uuid
import time
from datetime import datetime
import mysql.connector
import bcrypt
import os
import imghdr
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@post("/signup")
def _():

    
    try:
############### DEFINING THE USER, ADDRESS AND ZIPCODE #######################################
        user_id = str(uuid.uuid4())
        user_first_name = request.forms.get("user_first_name")
        user_last_name = request.forms.get("user_last_name")
        user_email = request.forms.get("user_email")
        user_created_at = str(int(time.time()))

        street_name = request.params.get("street_name")
        street_number = request.params.get("street_number")
        country = request.params.get("country")
        region = request.params.get("region")
        zipcode = request.params.get("zipcode")
        city = request.params.get("city")
        user_address_id = str(uuid.uuid4())

        image_id = str(uuid.uuid4())
        image_user = request.files.get("image_user")
        file_name, file_extension = os.path.splitext(image_user.filename)
        
        user_password = request.forms.get("user_password").encode("utf-8")
        salt = bcrypt.gensalt()
        password_hashed = bcrypt.hashpw(user_password, salt)


        if file_extension == ".jpg": file_extension = ".jpeg"

        image_name =f"{image_id}{file_extension}"
        image_user.save(f"images/user_image/{image_name}")

        imghdr_extension = imghdr.what(f"images/user_image/{image_name}")
        if file_extension != f".{imghdr_extension}":
            print("not an image")
            os.remove(f"images/user_image/{image_name}")
            return "removing the suspicious file..."

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

        sql = """INSERT INTO users (user_id, user_first_name, user_last_name, user_email, user_password, user_created_at, user_address_id, user_image_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (user_id,user_first_name,user_last_name, user_email, password_hashed, user_created_at, user_address_id,image_name, )
        cursor.execute(sql, val)

        print("user created")
        db.commit()

########## EMAIL ####################

        sender_email = "keatest.2022@gmail.com"
        receiver_email = user_email
        password = "Alanis123+"


        message = MIMEMultipart("alternative")
        message["Subject"] = "Tweeter account"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = """\
        Hi,
        Thank you.
        """

        html = """\
        <html>
            <body>
            <p>
                Hi,<br>
                Thank you for creating an account on Twitter.

                <h2>Enjoy!</h2>

                <em>Twitter</em>
            </p>
            </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            try:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print( "yes, email sent")
            except Exception as ex:
                print("ex")
                print("uppps... could not send the email")
        
    except Exception as ex:
        print(ex)
        db.rollback()
    finally:
        db.close()

    

        
            
    




