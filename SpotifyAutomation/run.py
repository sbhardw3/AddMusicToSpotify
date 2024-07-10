from youtube import Youtube
from spotify import SpotifyClient
from getToken import get_token, get_user_auth


def run():
    get_user_auth()

    auth_code = input("Enter the authorization code: ")

    token = get_token(auth_code)

    
    if token: 
        youtube_client = Youtube('D:\SpotifyAutomation\creds\client_secret.json')
        spotify_client = SpotifyClient(token)
        playlists = youtube_client.get_playlist()


        for index, playlist in enumerate(playlists):
            print(f"{index}:{playlist.title}")
        
        choice = int(input("Enter your choice: "))
        chosen_playlist = playlists[choice]
        print(f"You selected: {chosen_playlist.title}")

        songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)

    # print(f"Fetched songs: {songs}")


        print(f"Attempting to add {len(songs)}")


        for song in songs:
            spotify_song_id = spotify_client.search_song(song.artist, song.track)
            if spotify_song_id:
                added_song = spotify_client.add_song(spotify_song_id)
                if added_song:
                    print(f"Added {song.artist} - {song.track}")
                else:
                    print(f"Failed to add {song.artist} - {song.track}")
            else:
                print(f"No spotify ID found for {song.artist} - {song.track}")
    else:
        print("Failed to find a token")



run()
