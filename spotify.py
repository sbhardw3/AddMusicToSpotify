import requests
import urllib.parse
from rapidfuzz import fuzz


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def get_user_id(self):
        url = "https://api.spotify.com/v1/me"

        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {self.api_token}"}
        )

        response.raise_for_status()

        return response.json()["id"]

    def create_playlist(self, user_id, playlist_name):
        url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

        response = requests.post(
            url,
            json={
                "name": playlist_name,
                "description": "Created from YouTube playlist",
                "public": False
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

        response.raise_for_status()

        return response.json()["id"]

    def search_song(self, title):
        try:
            query = urllib.parse.quote(title)
            url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=10"

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }

            response = requests.get(url, headers=headers)
            response.raise_for_status()

            results = response.json().get("tracks", {}).get("items", [])

            best_score = 0
            best_track_id = None

            for item in results:
                spotify_track = item["name"]
                spotify_artist = item["artists"][0]["name"]

                combined_spotify = f"{spotify_track} {spotify_artist}"

                score = fuzz.token_set_ratio(
                    title.lower(),
                    combined_spotify.lower()
                )

                if score > best_score:
                    best_score = score
                    best_track_id = item["id"]

            if best_score > 60:
                return best_track_id

            return None

        except requests.exceptions.RequestException as e:
            print(f"Error searching song: {e}")
            return None

    def add_song(self, playlist_id, song_id):
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

        response = requests.post(
            url,
            json={
                "uris": [f"spotify:track:{song_id}"]
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

        response.raise_for_status()

        return response.ok