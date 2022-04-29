from bottle import  get, request, view, response

@get("/login")
@view("login")
def _():
    response.set_header("Cache-Control", "no-cache, no-store, must-revalidate")

    error = request.params.get("error")
    user_email = request.params.get("user_email")

    return dict(error=error, user_email = user_email)

