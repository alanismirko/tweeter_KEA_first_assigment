

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'


COOKIE_SECRET = "secret key"

USER_NAME_MIN_MAX  = '^[a-zA-Z]{2,50}$'

PRODUCTION_CONN = {
            "host":"keatest2020web.mysql.eu.pythonanywhere-services.com",
            "user": "keatest2020web",
            "password": "MySqLpassword",
            "database": "keatest2020web$tweeterdb",
            }

DEVELOPMENT_CONN = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }