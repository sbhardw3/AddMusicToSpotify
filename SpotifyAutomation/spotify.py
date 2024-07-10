import requests
import urllib.parse


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def search_song(self,artist,track):
        try:
            track = track.split("[")[0].strip()


            query = urllib.parse.quote(f"{artist}{track}")
            url = f"http://api.spotify.com/v1/search?q={query}&type=track"

            #print(f"Searching: {url}")

            
            headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_token}"
            }
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            response_json = response.json()
            

            results = response_json.get("tracks", {}).get("items", [])
            if results:
                #let's assume the first track in the list is the song we want
                return results[0]['id']
            else:
                raise Exception(f"No song found for {artist} = {track}")
            
        except requests.exceptions.RequestException as e:
            print (f"Error searching song: {e}")
            return None
        
        except (KeyError, ValueError) as r:
            print(f"Error parsing JSON response: {r}")
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
    
    
