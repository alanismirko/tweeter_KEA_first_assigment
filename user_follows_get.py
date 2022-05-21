from bottle import view, get, request, response
import g
import mysql
import json

@get("/following")
@get("/followers")
@view("user_follows")
def _():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
    user_profile_email = request.params.get("user_profile_email")

    error = request.params.get("error")
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")
    tabs = g.TABS
    reccomendations = g.RECOMMENDATIONS
    trends = g.TRENDS

    try:
        import production
        db_config = g.PRODUCTION_CONN
    except Exception as ex:
        print(ex)
        db_config = g.DEVELOPMENT_CONN


    try:
        print(user_profile_email)

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)
    
        sql = """SELECT * FROM follows WHERE user_email_initiator = %s"""
        cursor.execute(sql, (user_profile_email,))
        follows = cursor.fetchall()

        sql = """SELECT * FROM follows WHERE user_email_receiver = %s"""
        cursor.execute(sql, (user_profile_email,))
        followers = cursor.fetchall()

        sql = """SELECT * FROM users  WHERE user_email =%s """
        cursor.execute(sql, (user_profile_email,))
        users = cursor.fetchall() 
        db.commit()
    except Exception as ex:
        print(ex)
        response.status = 500

    finally:
        db.close()

    return dict(users= users, user_profile_email = user_profile_email, error=error, tweet_description=tweet_description,follows=follows,followers=followers, tweet_title=tweet_title, tabs=tabs, reccomendations=reccomendations, trends=trends)


@get("/myfollows")
@view("my_follows")
def _():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")

    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    error = request.params.get("error")
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")
    tabs = g.TABS
    reccomendations = g.RECOMMENDATIONS
    trends = g.TRENDS

    try:
        import production
        db_config = g.PRODUCTION_CONN
    except Exception as ex:
        print(ex)
        db_config = g.DEVELOPMENT_CONN


    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)
    
        sql = """SELECT * FROM follows WHERE user_email_initiator = %s"""
        cursor.execute(sql, (user_email,))
        follows = cursor.fetchall()

        sql = """SELECT * FROM follows WHERE user_email_receiver = %s"""
        cursor.execute(sql, (user_email,))
        followers = cursor.fetchall()

        args=[user_email]
        cursor.callproc('GetUserByEmail', args)
        for result in cursor.stored_results():
            users = result.fetchall()
        db.commit()
        response.status = 200

    except Exception as ex:
        print(ex)
        response.status = 500

    finally:
        db.close()

    return dict(users= users, user_email = user_email, error=error, tweet_description=tweet_description,follows=follows,followers=followers, tweet_title=tweet_title, tabs=tabs, reccomendations=reccomendations, trends=trends)
