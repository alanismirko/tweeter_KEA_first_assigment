from bottle import  get, view, request, redirect
import g

@get("/myprofile")
@view("myprofile")

def _():
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    error = request.params.get("error")
    tweet_title = request.forms.get("tweet_title")
    tweet_description = request.forms.get("tweet_description")
    return dict(user_email=user_email, error=error, tweet_title=tweet_title, tweet_description=tweet_description)