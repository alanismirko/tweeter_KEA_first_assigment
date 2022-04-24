from bottle import post, request, view, redirect
import g
import mysql

@post("/follow_user")
def _():
    user_profile_email = request.params.get("user_profile_email")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)

    try:
        import production
        db_config = g.PRODUCTION_CONN
    except Exception as ex:
        print(ex)
        db_config = g.DEVELOPMENT_CONN

    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)
    
        sql = """INSERT INTO follows (user_email_initiator, user_email_receiver ) VALUES (%s, %s)"""
        val = (user_email, user_profile_email)
        
        cursor.execute(sql, val)
        print("users are following")

        db.commit()

    except Exception as ex:
        print(ex)
    finally:
        db.close()
    return redirect("/following")
    
