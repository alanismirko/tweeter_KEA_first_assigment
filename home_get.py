from bottle import  get, view, request, redirect
import g

@get("/home")
@view("home")
def _():
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    user_session_id = request.get_cookie("uuid4")

    if user_session_id not in g.SESSIONS:
        return redirect("/login")
    


    return dict( user_email=user_email)
    