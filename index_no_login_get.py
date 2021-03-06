from bottle import get, view, request, response
import mysql
import mysql.connector
import g

@get("/")
@view("index_tweets")
def _():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")

    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")
    image_tweet = request.files.get("image_tweet")
        
###################### CONNECTING TO THE DATABASE ########################
    try:
        import production
        db_config = g.PRODUCTION_CONN

    except Exception as ex:
        print(ex)
        db_config = g.DEVELOPMENT_CONN


    try:

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)
        cursor.callproc('GetAllTweets')
        for result in cursor.stored_results():
            tweets = result.fetchall()

        db.commit()
        response.status = 200

    except Exception as ex:
        print(ex)
        response.status = 500

    finally:
        db.close()
    return dict(  tweet_description=tweet_description, tweet_title=tweet_title,  image_tweet = image_tweet, tweets= tweets)


