from bottle import  post, request, redirect
import g
import re
import uuid

@post("/signup")
def _():

    user_id = str(uuid.uuid4())
    user_first_name = request.forms.get("user_first_name")
    user_last_name = request.forms.get("user_last_name")
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")

    if not request.forms.get("user_email"):
        return redirect(f"/signup?error=user_email&user_first_name={user_first_name}&user_last_name={user_last_name}")
    if not re.match(g.REGEX_EMAIL,user_email):
        return redirect(f"/signup?error=user_email&user_first_name={user_first_name}&user_last_name={user_last_name}")

    if not user_password:
        return redirect(f"/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
    if len(user_password) < 6:
        return redirect(f"/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
    if len(user_password) > 50:
        return redirect(f"/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")

    if len(user_first_name) < 2:
        return redirect(f"/signup?error=user_first_name&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
    if len(user_last_name) < 2:
        return redirect(f"/signup?error=user_last_name&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
   

    user = {"user_id":user_id, "user_first_name":user_first_name, "user_last_name":user_last_name, "user_email": user_email, "user_password":user_password}

    g.USERS.append(user)
    return redirect("/login")
