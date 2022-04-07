from bottle import default_app, run, get, static_file, view, request
import json
import mysql.connector

#########  IMPORTS VIEWS ##############
import g    

import login_get   #GET
import signup_get  #GET
import logout_get  #GET
import tweet_get_all #GET
import mytweet_get
import search_tweet
import index_no_login_get


import signup_post    #POST
import login_post     #POST
import tweet_post     #POST
import tweet_delete_by_id   #POST
import tweet_update   #POST

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

#############  IMAGES  #################
@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")

#################################

try:
    import production
    application = default_app()
except Exception as ex:
    print(ex)
run ( host="127.0.0.1", port=8888, debug=True, reloader=True )

#################################
