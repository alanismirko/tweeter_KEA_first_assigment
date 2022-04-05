from bottle import  get, view, request


@get("/signup")
@view("signup")
def _():
    error = request.params.get("error")
    user_first_name = request.params.get("user_first_name")
    user_last_name = request.params.get("user_last_name")
    user_email = request.params.get("user_email")
    street_name = request.params.get("street_name")
    street_number = request.params.get("street_number")
    country = request.params.get("country")
    region = request.params.get("region")
    zipcode = request.params.get("zipcode")
    city = request.params.get("city")
    return dict(error=error,country=country, city=city, zipcode=zipcode, region=region, street_number = street_number, street_name=street_name,user_first_name=user_first_name, user_last_name=user_last_name, user_email=user_email)
    
