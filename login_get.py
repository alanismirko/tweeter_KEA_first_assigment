from bottle import run, get, post, view

@get("/login")
@view("login")
def _():
    return 