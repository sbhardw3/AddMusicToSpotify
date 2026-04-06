# app.py
from flask import Flask, redirect, render_template, request
from youtube import Youtube
from spotify import SpotifyClient
import os
import base64
from requests import post
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:5000/callback"

youtube_client = None
spotify_client = None
playlists = []
token = None

# --- Spotify OAuth functions ---
def get_token(auth_code):
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_str.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI
    }
    result = post(url, headers=headers, data=data)
    return result.json()["access_token"]

@app.route("/login_spotify")
def login_spotify():
    encoded_redirect = urllib.parse.quote(REDIRECT_URI, safe="")
    url = (
        f"https://accounts.spotify.com/authorize?"
        f"response_type=code&client_id={CLIENT_ID}"
        f"&scope=playlist-modify-private playlist-modify-public"
        f"&redirect_uri={encoded_redirect}"
    )
    return redirect(url)

@app.route("/callback")
def callback():
    global token, youtube_client, spotify_client, playlists
    code = request.args.get("code")
    token = get_token(code)
    spotify_client = SpotifyClient(token)
    youtube_client = Youtube("creds/client_secret.json")
    playlists = youtube_client.get_playlist()
    return redirect("/")

# --- Homepage ---
@app.route("/")
def home():
    global playlists
    if not youtube_client:
        return redirect("/login_spotify")
    return render_template("index.html", playlists=playlists)

# --- Select playlist ---
@app.route("/select_playlist", methods=["POST"])
def select_playlist():
    playlist_id = request.form["playlist_id"]
    songs = youtube_client.get_videos_from_playlist(playlist_id)
    return render_template("songs.html", songs=songs, playlist_id=playlist_id)

def get_playlist_name_by_id(playlist_id):
    for playlist in playlists:
        if playlist.id == playlist_id:
            return playlist.title
    return "Transferred YouTube Playlist"


# --- Transfer songs ---
@app.route("/transfer_playlist", methods=["POST"])
def transfer_playlist():
    playlist_id = request.form["playlist_id"]
    songs = youtube_client.get_videos_from_playlist(playlist_id)

    playlist_name = "Transferred Youtube Playlist"
    user_id = spotify_client.get_user_id()
    spotify_playlist_id = spotify_client.create_playlist(user_id, playlist_name)

    results = []

    for song in songs:
        spotify_id = spotify_client.search_song(song.title)

        if spotify_id:
            added = spotify_client.add_song(spotify_playlist_id, spotify_id)
            status = "Added" if added else "Failed"
        else:
            status = "Not found on Spotify"

        results.append({"title": song.title, "status": status})

    return render_template("transfer_result.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)