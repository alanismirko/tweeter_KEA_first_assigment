from distutils.log import error
from bottle import response, redirect
import re

##############################
_errors = {
  "en_server_error":"server error",
}

def _send(status = 400, error_message = "unknown error"):
  response.status = status
  print({"info":error_message})

def _is_name(text=None, language="en"):
    min,max = 2,20
    errors ={
        "en": f"name {min} to {max} characters. No spaces"
    }
    if not text: return None, errors[language]
    text = re.sub("[\n\t]*", "", text)
    text = re.sub(" +", " ", text)
    text = text.strip()
    if len(text) < min or len(text) > max : return None, errors[language]
    return text, None