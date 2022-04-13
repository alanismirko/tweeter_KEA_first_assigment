from bottle import get, view, request
import mysql

@get("/")
@view("index_tweets")
def _():
    try:
        tweet_description = request.params.get("tweet_description")
        tweet_title = request.params.get("tweet_title")
        image_tweet = request.files.get("image_tweet")
        
###################### CONNECTING TO THE DATABASE ########################
        db_config = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)
        cursor.execute("""SELECT * FROM tweets """)
        tweets = cursor.fetchall() 

    except Exception as ex:
        print(ex)
    finally:
        db.close()
    return dict(  tweet_description=tweet_description, tweet_title=tweet_title,  image_tweet = image_tweet, tweets= tweets)

