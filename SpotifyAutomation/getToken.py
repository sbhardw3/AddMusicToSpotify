from dotenv import load_dotenv
import os 
import base64
import json
from requests import post
import urllib.parse

load_dotenv()

#This is code that is provided by the Spotify API
#to get access to there token for use of the API

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = "http://localhost:8080/callback"

def get_user_auth():
    auth_url = (
        f"https://accounts.spotify.com/authorize?response_type=code"
        f"&client_id={client_id}&scope=user-library-modify"
        f"&redirect_uri={urllib.parse.quote(redirect_uri)}"
    )

    print(f"Go to the following link for authorization: {auth_url}")

def get_token(auth_code):
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    data = {"grant_type" : "authorization_code", "code" : auth_code, "redirect_uri" : redirect_uri}
    result = post(url, headers = headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token



