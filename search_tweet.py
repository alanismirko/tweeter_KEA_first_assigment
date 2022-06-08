from bottle import post, request, redirect, get, view
import g
import uuid
import time
from datetime import datetime
import mysql.connector


#SEARCH PEOPLE
@post("/search_users")
@view("search")
def _():
    
###################### VARIABLES #######################################
        
    search_term = request.forms.get("search_term")
    user_session_id = request.get_cookie("uuid4")
    error = request.params.get("error")
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    user_session_id = request.get_cookie("uuid4")





    tabs = g.TABS
    reccomendations = g.RECOMMENDATIONS
    trends = g.TRENDS


###################### CONNECTING TO THE DATABASE ########################
    try:
        import production
        db_config = g.PRODUCTION_CONN

    except Exception as ex:
        print(ex)
        db_config = g.DEVELOPMENT_CONN
    
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)

        sql = """ SELECT user_first_name, user_last_name, user_image_id FROM users WHERE 
                    MATCH (user_first_name, user_last_name)
                    AGAINST (%s IN NATURAL LANGUAGE MODE)
                    ORDER BY user_first_name ASC"""
        cursor.execute(sql, (search_term,))
        searchResults = cursor.fetchall()
        print(searchResults) 

        sql = """SELECT * FROM users  WHERE user_email =%s """
        cursor.execute(sql, (user_email,))
        users = cursor.fetchall() 


        sql_sessions=""" SELECT * FROM sessions WHERE session_id =%s"""
        cursor.execute(sql_sessions, (user_session_id,))
        session = cursor.fetchone()
        print(session)

        db.commit()
    except Exception as ex:
        print(ex)
    finally:
        db.close()

###################### RETURN ########################
    if session is None:
            return redirect("/login")


    return dict(searchTerm=search_term,searchResults = searchResults, tabs=tabs, reccomendations = reccomendations, trends = trends, error = error, tweet_description = tweet_description,
    tweet_title=tweet_title, users=users)



