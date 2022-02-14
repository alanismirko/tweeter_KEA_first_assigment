from bottle import  get, request, view

@get("/login")
@view("login")
def _():
    error = request.params.get("error")
    user_email = request.params.get("user_email")
    user_first_name = request.params.get("user_first_name")
    user_last_name = request.params.get("user_last_name")
    return dict(error=error, user_first_name=user_first_name, user_last_name=user_last_name, user_email = user_email)