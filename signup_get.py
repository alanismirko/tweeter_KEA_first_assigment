from bottle import  get, view, request


@get("/signup")
@view("signup")
def _():
    error = request.params.get("error")
    user_first_name = request.params.get("user_first_name")
    user_last_name = request.params.get("user_last_name")
    user_email = request.params.get("user_email")
    return dict(error=error, user_first_name=user_first_name, user_last_name=user_last_name, user_email=user_email)
    
