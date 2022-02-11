from bottle import run, get, post, view

@get("/tweets")
@view("tweets")
def _():
    return 