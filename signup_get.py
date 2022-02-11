from bottle import run, get, post, view

@get("/signup")
@view("signup")
def _():
    return 