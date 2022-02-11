from bottle import run, get, post, view

#########  IMPORTS VIEWS ##############
import login_get   #GET
import signup_get  #GET
import tweets_get  #GET

#################################
run ( host="127.0.0.1", port=8888, debug=True, reloader=True )