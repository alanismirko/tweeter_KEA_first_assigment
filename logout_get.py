from bottle import get, request, redirect
import g

@get("/logout")
def _():
    user_session_id = request.get_cookie("uuid4")
    g.SESSIONS.remove(user_session_id)
    return redirect("/login")