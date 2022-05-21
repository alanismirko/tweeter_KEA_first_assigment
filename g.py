

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'


COOKIE_SECRET = "secret key"

USER_NAME_MIN_MAX  = '^[a-zA-Z]{2,50}$'

TABS =  [
    {"icon": "fas fa-home fa-fw", "title": "Home", "id":"home", "href": "/index"},
    {"icon": "fas fa-hashtag fa-fw", "title": "Explore", "id": "explore", "href":"/explore"},
    {"icon": "far fa-bell fa-fw", "title": "Notifications", "id": "notifications", "href":"/index"},
    {"icon": "far fa-envelope fa-fw", "title": "Messages", "id": "messages", "href":"/index"},
    {"icon": "far fa-bookmark fa-fw", "title": "Bookmarks", "id": "bookmarks", "href":"/index"},
    {"icon": "fas fa-clipboard-list fa-fw", "title": "Lists", "id": "lists", "href":"/index"},
    {"icon": "far fa-user fa-fw", "title": "Profile", "id": "profile", "href":"/myprofile"},
    {"icon": "fas fa-ellipsis-h fa-fw", "title": "More", "id": "more", "href":"/index"},
    {"icon": "fa fa-sign-out fa-fw", "title": "Logout", "id": "logout", "href":"/logout"}
    ]

TRENDS = [
  {"category": "Music", "title": "We Won", "tweets_counter": "135K"},
  {"category": "Pop", "title": "Blue Ivy", "tweets_counter": "40k"},
  {"category": "Trending in US", "title": "Denim Day", "tweets_counter": "40k"},
  {"category": "Trending in UK", "title": "Football cup", "tweets_counter": "300k"},
  {"category": "Croatia summer", "title": "Sunny days", "tweets_counter": "150k"},
  {"category": "Trending in DK", "title": "Lakrids", "tweets_counter": "150k"}
]

RECOMMENDATIONS =[
  {"src":"../images/right_images/3.jpg", "user_first_name":"Elon", "user_last_name":"Musk", "user_name":"elonmusk"},
  {"src":"../images/right_images/2.jpg", "user_first_name":"Joe", "user_last_name":"Biden", "user_name":"joebiden"},
  {"src":"../images/right_images/6.jpg", "user_first_name":"Barack", "user_last_name":"Obama", "user_name":"baracobama"}
]


DEVELOPMENT_CONN = {
        "host": "localhost",
        "user":"root",
        "database": "tweeterdbexam",
        "password": "1234"
        }

PRODUCTION_CONN = {
            "host":"keatest2020web.mysql.eu.pythonanywhere-services.com",
            "user": "keatest2020web",
            "password": "MySqLpassword",
            "database": "keatest2020web$tweeterdb"
            }