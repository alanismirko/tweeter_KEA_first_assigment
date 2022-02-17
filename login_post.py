from bottle import request, redirect, post, response
import g 
import re
import uuid
import jwt


@post("/login")
def _():

    user_email = request.forms.get("user_email")
    response.set_cookie("user_email", user_email, secret=g.COOKIE_SECRET)

    user_password = request.forms.get("user_password")
    user_session_id = str(uuid.uuid4())
    encoded_jwt = jwt.encode({"uuid4": user_session_id, "user_email":user_email}, "secret key", algorithm="HS256")

    response.set_cookie("encoded_jwt", encoded_jwt)
    response.set_cookie("uuid4", user_session_id)


    g.SESSIONS.append(user_session_id)

    for user  in g.USERS:
        if user["user_email"] == user_email and user["user_password"] == user_password  :
            return redirect(f"/home")
    return redirect(f"/login?error=wrong_credentials")

