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
    print(search_term)


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

        sql = """ SELECT  user_first_name,  user_last_name FROM users WHERE user_first_name LIKE %s"""
        term = [search_term + '%']
        cursor.execute(sql, term)
        searchResults = cursor.fetchall()
        print(searchResults) 

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
    # if session is None:
    #         return redirect("/login")


    return dict(searchResults = searchResults)



