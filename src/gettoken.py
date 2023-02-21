import requests
import webbrowser
from urllib.parse import urlencode
import base64

AUTH_URL = 'https://accounts.spotify.com/api/token'

def authenticate (CLIENT_ID, CLIENT_SECRET):

    auth_headers = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": "http://localhost:8888/callback",
        "scope": "user-library-read user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private" 
    }

    webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

    code = str(input("code: "))

    encoded_credentials = base64.b64encode(CLIENT_ID.encode() + b':' + CLIENT_SECRET.encode()).decode("utf-8")

    token_headers = {
        "Authorization": "Basic " + encoded_credentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8888/callback"
    }

    r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

    token = r.json()["access_token"]
    
    return token

