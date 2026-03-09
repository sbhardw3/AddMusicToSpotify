from dotenv import load_dotenv
import os
import base64
from requests import post
import urllib.parse
from flask import Flask, request, redirect

from youtube import Youtube
from spotify import SpotifyClient

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = "http://127.0.0.1:5000/callback"

app = Flask(__name__)

token = None
youtube_client = None
spotify_client = None
playlists = []


def get_token(auth_code):

    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": redirect_uri
    }

    result = post(url, headers=headers, data=data)
    json_result = result.json()

    return json_result["access_token"]


@app.route("/")
def login():

    encoded_redirect = urllib.parse.quote(redirect_uri, safe='')

    auth_url = (
        f"https://accounts.spotify.com/authorize?response_type=code"
        f"&client_id={client_id}"
        f"&scope=user-library-modify"
        f"&redirect_uri={encoded_redirect}"
    )

    return redirect(auth_url)


@app.route("/callback")
def callback():
    global token, youtube_client, spotify_client, playlists

    code = request.args.get("code")
    token = get_token(code)

    youtube_client = Youtube(r"C:\SpotifyAutomation\creds\client_secret.json")
    spotify_client = SpotifyClient(token)

    # Fetch playlists now so the homepage can show them
    playlists = youtube_client.get_playlist()

    # Redirect to your home page (Flask template will handle design)
    return redirect("/")


@app.route("/playlist/<int:index>")
def show_playlist(index):

    playlist = playlists[index]

    songs = youtube_client.get_videos_from_playlist(playlist.id)

    html = f"<h2>{playlist.title}</h2>"

    for s in songs:
        html += f"<p>{s.artist} - {s.track}</p>"

    html += f"""
        <form action="/transfer/{index}" method="post">
            <button type="submit">Transfer Songs</button>
        </form>
    """

    return html


@app.route("/transfer/<int:index>", methods=["POST"])
def transfer(index):

    playlist = playlists[index]
    songs = youtube_client.get_videos_from_playlist(playlist.id)

    html = "<h2>Transfer Result</h2>"

    for song in songs:

        spotify_id = spotify_client.search_song(song.artist, song.track)

        if spotify_id:
            spotify_client.add_song(spotify_id)
            html += f"<p>Added {song.artist} - {song.track}</p>"
        else:
            html += f"<p>Could not find {song.artist} - {song.track}</p>"

    return html

