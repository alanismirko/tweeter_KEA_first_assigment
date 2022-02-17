from bottle import post, redirect, request
import g

@post("/delete_tweet/<tweet_id>")
def _(tweet_id):

    tweet_id = request.forms.get("tweet_id")
    for index, tweet in enumerate(g.TWEETS):
        if tweet["tweet_id"] == tweet_id:
            g.TWEETS.pop(index)
            return redirect("/tweets")
    return redirect("/tweets")
    