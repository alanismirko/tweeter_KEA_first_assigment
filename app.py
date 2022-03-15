from bottle import default_app, run, get, static_file
import json
import mysql.connector

#########  IMPORTS VIEWS ##############
import g           

import login_get   #GET
import signup_get  #GET
import tweet_get  #GET
import home_get    #GET
import logout_get  #GET
import profile_get  #GET

import signup_post    #POST
import login_post     #POST
import tweet_post     #POST
import tweet_delete   #POST
import tweet_update   #POST
import profile_update  #POST

#########  CSS #################

@get("/app.css")
def _():
    return static_file("app.css", root="./style")

@get("/style.css")
def _():
    return static_file("style.css", root="./style")

#################################


db_config = {
        "host": "localhost",
        "user":"root",
         "database": "tweeterdb",
        "password": "1234",
    }

#################################
db = mysql.connector.connect(**db_config)
cursor = db.cursor()


try:
    import production
    application = default_app()
except Exception as ex:
    print(ex)
run ( host="127.0.0.1", port=8888, debug=True, reloader=True )

#################################
