# 🎵 YouTube → Spotify Playlist Transfer

A Python-based tool that allows you to transfer your YouTube playlists to Spotify. It uses **Flask** for a web interface and integrates the **YouTube Data API** and **Spotify Web API**.

---

## **Features**

- Authenticate with Spotify and YouTube securely
- View your YouTube playlists directly in a web interface
- Select a playlist and view all songs
- Transfer songs to your Spotify library
- Clean YouTube video titles automatically for accurate Spotify searches

---

## **Prerequisites**

1. **Python 3.11+** (tested on Python 3.13)  
2. **Spotify Developer Account**  
   - [Create an app](https://developer.spotify.com/dashboard/applications)  
   - Add redirect URI: `http://127.0.0.1:5000/callback`  
3. **Google Developer Account**  
   - [Create OAuth client](https://console.developers.google.com/)  
   - Enable YouTube Data API v3  
   - Download `client_secret.json`  
4. Install required Python packages:
```bash
pip install -r requirements.txt
