import os
from youtube import Youtube
from spotify import SpotifyClient

def run():
    youtube_client = Youtube('./creds/client_secret.json')
    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTH_TOKEN"))
    playlists = youtube_client.get_playlist()


    for index, playlist in enumerate(playlists):
        print(f"{index}:{playlist.title}")
    
    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice]
    print(f"You selected: {chosen_playlist.title}")


    songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
    print(f"Attempting to add {len(song)}")

    for song in songs:
        spotify_song_id = spotify_client.search_song(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song(spotify_song_id)
            if added_song:
                print(f"Added {song.artist}")