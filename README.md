# YouTube → Spotify Playlist Transfer

A Python-based web application that synchronizes YouTube playlists with Spotify.
The application uses Flask for the backend and integrates the YouTube Data API and Spotify Web API to automate playlist creation, matching, and syncing.

---

## Features

* OAuth authentication with Spotify and YouTube
* Fetch and display user YouTube playlists
* View songs from a selected playlist
* Create or reuse Spotify playlists based on YouTube playlist names
* Idempotent sync logic (no duplicate playlist creation)
* Duplicate detection (prevents adding the same track twice)
* Fuzzy matching using RapidFuzz for accurate song mapping
* Regex-based title cleaning for noisy YouTube metadata
* Transfer results with detailed status (Added / Already Present / Not Found)
* Summary dashboard for transfer results
* Loading indicators for improved user experience
* Unit testing with pytest
* CI pipeline using GitHub Actions

---

## How It Works

1. User authenticates with Spotify
2. Application retrieves YouTube playlists
3. User selects a playlist
4. Video titles are extracted and cleaned
5. Songs are searched on Spotify using full-title matching
6. RapidFuzz selects the best match
7. App checks if a matching Spotify playlist already exists
8. Existing playlist is reused or a new one is created
9. Duplicate tracks are skipped
10. New tracks are added to the playlist

---

## Tech Stack

* Backend: Python, Flask
* APIs: YouTube Data API v3, Spotify Web API
* Matching: RapidFuzz (token-based similarity)
* Data Processing: Regex-based title cleaning
* Testing: pytest
* CI/CD: GitHub Actions
* Frontend: HTML, CSS (Flask templates)

---

## Prerequisites

### Python

* Python 3.11 or higher

---

### Spotify Developer Setup

* Go to: https://developer.spotify.com/dashboard/applications
* Create an application
* Add redirect URI: http://127.0.0.1:5000/callback
* Copy your Client ID and Client Secret

---

### YouTube API Setup

* Go to: https://console.developers.google.com/
* Create OAuth credentials
* Enable YouTube Data API v3
* Download credentials file and place it at:
  creds/client_secret.json

---

### Install Dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a `.env` file in the root directory:

CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret

---

## Running the Application

python app.py

Open in browser:
http://127.0.0.1:5000

---

## Usage

1. Log in with Spotify
2. Select a YouTube playlist
3. Review extracted songs
4. Click "Transfer Songs"
5. Playlist is created or reused on Spotify
6. Songs are added without duplication
7. View transfer results and summary

---

## Example Flow

YouTube Playlist
↓
Extract Titles
↓
Clean Titles (Regex)
↓
Spotify Search
↓
Fuzzy Matching (RapidFuzz)
↓
Find or Create Playlist
↓
Skip Duplicates
↓
Add New Songs

---

## Testing

Run tests locally:

python -m pytest

CI is configured using GitHub Actions to automatically run tests on push.

---

## Limitations

* Some songs may not match due to inconsistent YouTube titles
* Matching accuracy depends on metadata quality
* Large playlists may take longer due to API rate limits

---

## Future Improvements

* Scheduled auto-sync (background job)
* Advanced NLP-based matching
* Playlist diff view before syncing
* Progress bar for long transfers
* Deployment with persistent backend

---

## Author

Shiven Bhardwaj
