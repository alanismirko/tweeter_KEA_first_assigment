from bottle import default_app, run, get, static_file, view
import json
import mysql.connector

#########  IMPORTS VIEWS ##############
import g      

import index_get
import login_get   #GET
import signup_get  #GET
import logout_get  #GET
import profile_get  #GET

import signup_post    #POST
import login_post     #POST
import tweet_post     #POST
import tweet_delete_by_id   #POST
import tweet_update   #POST
import profile_update  #POST

#########  CSS #################

@get("/app.css")
def _():
    return static_file("app.css", root="./style")

@get("/style.css")
def _():
    return static_file("style.css", root="./style")

@get("/app.css")
def _():
  return static_file("app.css", root=".")

#############  JS  #################
@get("/app.js")
def _():
  return static_file("app.js", root=".")


#################################

try:
    import production
    application = default_app()
except Exception as ex:
    print(ex)
run ( host="127.0.0.1", port=8888, debug=True, reloader=True )

#################################
