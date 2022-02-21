from bottle import post, request, redirect
import g

@post("/tweet_update/<tweet_id>")
def _(tweet_id):
    tweet_id = request.forms.get("tweet_id")
    tweet_title = request.forms.get("tweet_title")
    tweet_description = request.forms.get("tweet_description")
    user_session_id = request.get_cookie("uuid4")

    if len(tweet_title) < 1:
        return redirect(f"/tweets?error=tweet_title&tweet_description={tweet_description}")
    if len(tweet_description) < 1:
        return redirect(f"/tweets?error=tweet_description&tweet_title={tweet_title}")

    if user_session_id not in g.SESSIONS:
        return redirect("/login")
    

    for  tweet in g.TWEETS:
        if tweet["tweet_id"] == tweet_id:
            tweet.update({"tweet_title":tweet_title, "tweet_description": tweet_description})
    return redirect("/tweets")

