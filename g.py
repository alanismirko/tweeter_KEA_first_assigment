

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'


COOKIE_SECRET = "secret key"

USER_NAME_MIN_MAX  = '^[a-zA-Z]{2,50}$'

TABS =  [
    {"icon": "fas fa-home fa-fw", "title": "Home", "id":"home", "href": "/index"},
    {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore", "href":"/index"},
    {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications", "href":"/index"},
    {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages", "href":"/index"},
    {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks", "href":"/index"},
    {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists", "href":"/index"},
    {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile", "href":"/myprofile"},
    {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more", "href":"/index"},
    {"icon": "fa fa-sign-out fa-fw", "title": "Logout", "id": "logout", "href":"/logout"}
    ]


DEVELOPMENT_CONN = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdb",
        "password": "1234"
        }

PRODUCTION_CONN = {
            "host":"keatest2020web.mysql.eu.pythonanywhere-services.com",
            "user": "keatest2020web",
            "password": "MySqLpassword",
            "database": "keatest2020web$tweeterdb"
            }