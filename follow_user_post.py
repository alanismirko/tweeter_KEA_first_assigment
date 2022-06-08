from bottle import post, request, view, redirect, response
import g
import mysql
import mysql.connector


@post("/follow_user")
def _():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")

    user_profile_email = request.params.get("user_profile_email")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)

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
    
        sql = """INSERT INTO follows (user_email_initiator, user_email_receiver, status_id ) VALUES (%s, %s, %s)"""
        val = (user_email, user_profile_email, 2)
        
        cursor.execute(sql, val)
        print("users are following")

        db.commit()
        response.status = 200

    except Exception as ex:
        print(ex)
        response.status= 500

    finally:
        db.close()
        return redirect("/explore")    
