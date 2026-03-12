import os
import re
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import yt_dlp as youtube_dl
import google_auth_oauthlib
from cleaner import clean_title
import pickle

class Playlist(object):
    def __init__(self, id, title):
        self.id = id
        self.title = title 

class Song(object):
    def __init__(self, title):
        self.title = title

class Youtube(object):
   #This part of the code was picked from the Youtube API!!!
    def __init__(self, location):
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        creds_file = "creds/youtube_token.pkl"

        if os.path.exists(creds_file):
            with open(creds_file, "rb") as f:
                credentials = pickle.load(f)
        else:
            os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(location, scopes)
            credentials = flow.run_local_server(port=0)
            with open(creds_file, "wb") as f:
                pickle.dump(credentials, f)

        self.youtube = googleapiclient.discovery.build(
            "youtube", "v3", credentials=credentials
        )
      
    #Here youtube client has a function called playlists.list() thorugh which 
    #we can get access to various artists and songs 
    def get_playlist(self):
        request = self.youtube.playlists().list(
            part = "id , snippet",
            maxResults = 50, #I want the playlist to be 50 songs long
            mine= True #I should get my own playlist 
        )

        response = request.execute()

        playlists = [Playlist(item["id"], item["snippet"]["title"]) for item in response['items']]

        return playlists
    


    def get_videos_from_playlist(self, playlist_id):

        songs = []
        request = self.youtube.playlistItems().list(

            playlistId = playlist_id,
            part = "snippet",
            maxResults=50
        )

         
        response = request.execute()

        for item in response['items']:
            video_id = item["snippet"]["resourceId"]["videoId"]

            title = self.get_video_title(video_id)

            if title:
                songs.append(Song(title))
            else:
                print("Skipped:", video_id)

        return songs
    


    def get_artist_and_track(self, video_id):
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"

        video_info = youtube_dl.YoutubeDL({'quiet': True}).extract_info(youtube_url, download=False)

        title = video_info.get("title")
        title = clean_title(title)

        artist, track = self.extract_artist_and_track(title)

        #print(f"Video info for {video_id}: {video_info.get("title")}")

        return artist, track

    def get_video_title(self, video_id):

        youtube_url = f"https://www.youtube.com/watch?v={video_id}"

        video_info = youtube_dl.YoutubeDL({'quiet': True}).extract_info(
            youtube_url,
            download=False
        )

        title = video_info.get("title")

        if not title:
            return None

        title = clean_title(title)

        return title
        
    def extract_artist_and_track(self, title):

        title = title.lower()

        # normalize separators
        separators = ["|", "-", "—", "–"]

        for sep in separators:
            if sep in title:
                parts = [p.strip() for p in title.split(sep)]

                # Example: 295 | sidhu moose wala | the kidd
                if len(parts) >= 2:
                    track = parts[0]
                    artist = parts[1]

                    return artist, track

        # fallback heuristic
        words = title.split()

        # if title begins with a number like "295"
        if words and words[0].isdigit():
            track = words[0]
            artist = " ".join(words[1:3])  # guess first two words as artist
            return artist, track

        return None, None #If no pattern matches 

        

