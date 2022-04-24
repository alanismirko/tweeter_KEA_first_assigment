from bottle import get, view, request
import mysql
import g

@get("/")
@view("index_tweets")
def _():
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")
    image_tweet = request.files.get("image_tweet")
        
###################### CONNECTING TO THE DATABASE ########################
    try:
        db_config = g.PRODUCTION_CONN
    except Exception as ex:
        print("ex")
        db_config = g.DEVELOPMENT_CONN

    try:

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)
        cursor.execute("""SELECT * FROM tweets """)
        tweets = cursor.fetchall() 

        db.commit()
    except Exception as ex:
        print(ex)
    finally:
        db.close()
    return dict(  tweet_description=tweet_description, tweet_title=tweet_title,  image_tweet = image_tweet, tweets= tweets)

