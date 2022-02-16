from bottle import post, request, redirect, get, view
import g
import uuid

@post("/create_tweet")
def _():

    tweet_id = str(uuid.uuid4())
    tweet_title = request.forms.get("tweet_title")
    tweet_description = request.forms.get("tweet_description")
    tweet_id = request.forms.get("tweet_description")

    if len(tweet_title) < 1:
        return redirect(f"tweets?error=tweet_title_create&tweet_description={tweet_description}&tweet_title={tweet_title}")
    if len(tweet_description) < 1:
        return redirect(f"tweets?error=tweet_description_create&tweet_title={tweet_title}&tweet_description={tweet_description}")

    tweet = {"tweet_id": tweet_id, "tweet_title": tweet_title, "tweet_description":tweet_description}
    g.TWEETS.append(tweet)
    return redirect("/tweets")



