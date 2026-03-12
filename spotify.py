import requests
import urllib.parse
from rapidfuzz import fuzz


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

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
            


    def add_song(self,song_id):

        try: 
            url = "https://api.spotify.com/v1/me/tracks"
            response = requests.put(
                url,
                json={
                    "ids" : [song_id]
                },
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_token}"
                }
            )

            response.raise_for_status()

            return response.ok
        
        except requests.exceptions.RequestException as e:
            print(f"Error adding song: {e}")
            return False
    
    
