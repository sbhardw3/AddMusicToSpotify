# YouTube → Spotify Playlist Transfer

A Python web application that recreates YouTube playlists on Spotify.
The application uses Flask for the backend and integrates the YouTube
Data API and Spotify Web API to automate playlist transfer.

------------------------------------------------------------------------

## Features

-   OAuth authentication with Spotify and YouTube\
-   Fetch and display user YouTube playlists\
-   View songs from a selected playlist\
-   Create a new playlist on Spotify using the YouTube playlist name\
-   Automatically transfer songs to Spotify\
-   Fuzzy matching using RapidFuzz to handle inconsistent YouTube
    titles\
-   Regex-based title cleaning for improved matching accuracy\
-   Transfer results with success and failure status\
-   Loading indicators for better user experience

------------------------------------------------------------------------

## How It Works

1.  User authenticates with Spotify\
2.  Application retrieves YouTube playlists\
3.  User selects a playlist\
4.  Video titles are extracted and cleaned\
5.  Songs are searched on Spotify using full-title matching\
6.  RapidFuzz is used to select the best match\
7.  A new Spotify playlist is created\
8.  Matched songs are added to the playlist

------------------------------------------------------------------------

## Tech Stack

-   Backend: Python, Flask\
-   APIs: YouTube Data API v3, Spotify Web API\
-   Matching: RapidFuzz (token-based similarity)\
-   Data Processing: Regex-based title cleaning\
-   Frontend: HTML, CSS (Flask templates)

------------------------------------------------------------------------

## Prerequisites

### Python

-   Python 3.11 or higher

------------------------------------------------------------------------

### Spotify Developer Setup

-   Go to: https://developer.spotify.com/dashboard/applications\
-   Create an application\
-   Add redirect URI: http://127.0.0.1:5000/callback\
-   Copy your Client ID and Client Secret

------------------------------------------------------------------------

### YouTube API Setup

-   Go to: https://console.developers.google.com/\
-   Create OAuth credentials\
-   Enable YouTube Data API v3\
-   Download the credentials file and place it at:
    creds/client_secret.json

------------------------------------------------------------------------

### Install Dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

## Environment Variables

Create a `.env` file in the root directory:

CLIENT_ID=your_spotify_client_id\
CLIENT_SECRET=your_spotify_client_secret

------------------------------------------------------------------------

## Running the Application

python app.py

Open the application in your browser:

http://127.0.0.1:5000

------------------------------------------------------------------------

## Usage

1.  Log in with Spotify\
2.  Select a YouTube playlist\
3.  Review extracted songs\
4.  Click "Transfer Songs"\
5.  A new playlist is created on Spotify\
6.  View transfer results

------------------------------------------------------------------------

## Example Flow

YouTube Playlist\
↓\
Extract Titles\
↓\
Clean Titles (Regex)\
↓\
Spotify Search\
↓\
Fuzzy Matching (RapidFuzz)\
↓\
Create Spotify Playlist\
↓\
Add Songs

------------------------------------------------------------------------

## Limitations

-   Some songs may not match due to inconsistent naming on YouTube\
-   Matching accuracy depends on title quality\
-   Large playlists may take longer due to API requests

------------------------------------------------------------------------

## Future Improvements

-   Automatic playlist synchronization\
-   Improved matching accuracy using advanced NLP techniques\
-   Duplicate detection before adding songs\
-   Deployment to a cloud platform\
-   Enhanced UI with real-time progress updates

------------------------------------------------------------------------

## Author

Shiven Bhardwaj
