from bottle import  get, view, request, redirect, post, template
import g
import mysql

@get("/admin")
@view("admin")
def _():
###################### DEFINING THE VARIABLES ########################
    error = request.params.get("error")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    user_email_admin = request.forms.get("user_email")
    user_first_name = request.get_cookie("user_first_name", secret=g.COOKIE_SECRET)
    user_last_name = request.get_cookie("user_last_name", secret=g.COOKIE_SECRET)
    user_session_id = request.get_cookie("uuid4")
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")
    image_tweet = request.files.get("image_tweet")
    tweet_id_update = request.forms.get("tweet_id_update")

###################### CONNECTING TO THE DATABASE ########################
    try:
        db_config = g.PRODUCTION_CONN
    except Exception as ex:
        print("ex")
        db_config = g.DEVELOPMENT_CONN
        
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)

        
        sql = """SELECT * FROM tweets  """
        cursor.execute(sql,)
        tweets = cursor.fetchall() 

        sql_sessions=""" SELECT * FROM sessions WHERE session_id =%s"""
        cursor.execute(sql_sessions, (user_session_id,))
        session = cursor.fetchone()
        print(session)

        
        sql = """DELETE FROM sessions WHERE TIMESTAMPDIFF(MINUTE,session_created_at,NOW()) > 30; """
        cursor.execute(sql)
        print("User session is deleted")

        db.commit()

    except Exception as ex:
        print(ex)

    finally:
        db.close()

###################### RETURN - DICTIONARY ########################
    if session is None:
        return redirect("/login")
    if user_email != "admin@gmail.com":
        return redirect("/login")
    return dict( error = error, tweet_description=tweet_description, 
                    user_first_name=user_first_name, user_last_name=user_last_name, 
                    tweet_title=tweet_title, user_email=user_email, tweets = tweets, image_tweet = image_tweet)
