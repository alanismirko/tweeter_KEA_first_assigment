from bottle import post, request, redirect, get, view, response
import g
import mysql.connector
import tweet_like


@get("/tweets")
@get("/index")
@view("index")
def _():
###################### DEFINING THE VARIABLES ########################
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
    error = request.params.get("error")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")
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
        cursor.execute("""SELECT * FROM tweets """)
        tweets = cursor.fetchall() 

        sql_sessions=""" SELECT * FROM sessions WHERE session_id =%s"""
        cursor.execute(sql_sessions, (user_session_id,))
        session = cursor.fetchone()
        print(session)

        sql = """SELECT * FROM users  WHERE user_email =%s """
        cursor.execute(sql, (user_email,))
        users = cursor.fetchall() 
        print(users)

        sql = """DELETE FROM sessions WHERE TIMESTAMPDIFF(MINUTE,session_created_at,NOW()) > 30; """
        cursor.execute(sql)

        db.commit()
        response.status = 200

    except Exception as ex:
        print(ex)
        response.status = 500

    finally:
        db.close()

###################### RETURN - DICTIONARY ########################
        if session is None:
                return redirect("/login")
        return dict( error = error, tweet_description=tweet_description,  
                        tweet_title=tweet_title, user_email=user_email, tweets = tweets, tabs=tabs, users=users, reccomendations=reccomendations, trends = trends)