from bottle import post, view, request, redirect
import g
import json
import uuid

@post("/create_tweet")
def _():

    #VALIDATE
    tweet_id = str(uuid.uuid4())
    tweet_title = request.forms.get("tweet_title")
    tweet_description = request.forms.get("tweet_description")
    tweet_id = request.forms.get("tweet_description")

    tweet = {"tweet_id": tweet_id, "tweet_title": tweet_title, "tweet_description":tweet_description}
    g.TWEETS.append(tweet)
    return redirect("/tweets")