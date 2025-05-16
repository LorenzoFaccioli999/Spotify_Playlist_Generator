# 🎵 Spotify Top 100 Playlist Generator

This Python script automatically creates a private Spotify playlist populated with the top 100 Billboard songs from a specific historical date chosen by the user. It combines **web scraping** and **Spotify’s Web API** using `BeautifulSoup` and `Spotipy`.

## 📌 Project Overview

Given a date in the format `YYYY-MM-DD`, the script:
1. Scrapes the Billboard Hot 100 chart for that day.
2. Searches each track on Spotify using both song title and artist name.
3. Creates a new **private playlist** in the user’s Spotify account.
4. Adds all found tracks (up to 100) to the playlist.

It’s a great tool to relive the music of a particular day—be it your birthday, anniversary, or any date from the Billboard archives.

## 🔧 Technologies Used

- **BeautifulSoup** – for HTML parsing and data extraction from Billboard.com.
- **Spotipy** – Python wrapper for the Spotify Web API.
- **SpotifyOAuth** – for handling authentication and permissions.

## 🚀 How to Use

1. **Set up your Spotify Developer credentials:**
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Create an app and retrieve your `CLIENT_ID` and `CLIENT_SECRET`
   - Set your `REDIRECT_URI` (e.g., `http://example.com`)

2. **Install dependencies:**
   ```bash
   pip install beautifulsoup4 spotipy requests
