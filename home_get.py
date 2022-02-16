from bottle import  get, view, request, redirect
import g

@get("/home")
@view("home")
def _():
    error = request.forms.get("error")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    user_session_id = request.get_cookie("uuid4")
    tweet_description = request.forms.get("tweet_description")
    tweet_title = request.forms.get("tweet_title")

    if user_session_id not in g.SESSIONS:
        return redirect("/login")
    


    return dict( error=error, tweet_description=tweet_description, tweet_title=tweet_title, user_email=user_email)
    