from bottle import get, view, request
import mysql

@get("/")
@view("index_tweets")
def _():
    tweet_description = request.params.get("tweet_description")
    tweet_title = request.params.get("tweet_title")
    image_tweet = request.files.get("image_tweet")
        
###################### CONNECTING TO THE DATABASE ########################
    try:
        import production
        db_config = {
                "host":"keatest2020web.mysql.eu.pythonanywhere-services.com",
                "user": "keatest2020web",
                "password": "MySqLpassword",
                "database": "keatest2020web$tweeterdb",
        }
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(buffered=True)
        cursor.execute("""SELECT * FROM tweets """)
        tweets = cursor.fetchall() 

        db.commit()
    except Exception as ex:
        print(ex)
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

        db.commit()

    finally:
        db.close()
    return dict(  tweet_description=tweet_description, tweet_title=tweet_title,  image_tweet = image_tweet, tweets= tweets)

