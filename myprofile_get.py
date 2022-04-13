from bottle import get, view, request
import g

@get("/myprofile")
@view("myprofile")
def _():
    error = request.params.get("error")
    user_email = request.get_cookie("user_email", secret=g.COOKIE_SECRET)
    user_first_name = request.get_cookie("user_first_name", secret=g.COOKIE_SECRET)
    user_last_name = request.get_cookie("user_last_name", secret=g.COOKIE_SECRET)
    user_session_id = request.get_cookie("uuid4")
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")
    image_tweet = request.files.get("image_tweet")

    return dict( error = error, tweet_description=tweet_description, 
                    user_first_name=user_first_name, user_last_name=user_last_name, 
                    tweet_title=tweet_title, user_email=user_email, image_tweet = image_tweet)
