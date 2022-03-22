from bottle import get, post, view

@get("/sessions")
def _():
    return