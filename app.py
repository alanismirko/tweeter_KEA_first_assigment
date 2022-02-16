from bottle import run, get, post, view, static_file

#########  IMPORTS VIEWS ##############
import g           

import login_get   #GET
import signup_get  #GET
import tweets_get  #GET
import home_get    #GET
import logout_get  #GET

import signup_post    #POST
import login_post     #POST
import tweet_post     #POST
import tweet_delete   #POST
import tweet_update   #POST

#########  CSS ##############

@get("/app.css")
def _():
    return static_file("app.css", root=".")

#################################
run ( host="127.0.0.1", port=8888, debug=True, reloader=True )