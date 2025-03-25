# Music Downloader

A Python tool that allows you to download MP3 files from YouTube by simply providing the name of the song you want!

<br>

## Overview

This repository contains two versions of a music downloader:

1. **Simple Music Downloader** - Basic functionality to search and download songs from YouTube
2. **Experimental Music Downloader** - Advanced version with AI-powered audio trimming to extract just the musical content, leaving out the intro and outro segments consiisting of sponsors, branding or advertisements.

<br>

## Features

### Simple Music Downloader
- Search YouTube for songs by name
- Download audio tracks as MP3 files
- Simple and straightforward implementation

### Experimental Music Downloader
- AI-powered audio content analysis using Google's Gemini model
- Automatically detects when the actual music begins and ends
- Trims out non-musical segments (ads, talking, etc.)
- Creates clean MP3 files with just the music

<br>

## Requirements
```
- pytubefix
- youtube_search
- google-generativeai (for experimental version)
- moviepy (for experimental version)
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Music_Downloader.git
   cd Music_Downloader
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. For the experimental version, install additional dependencies:
   ```
   pip install google-generativeai moviepy
   ```

4. For the experimental version, you need to set up a Google API key for the Gemini model.

<br>

## How It Works

### Simple Version
The simple downloader searches YouTube for the song name, gets the URL of the first result, and downloads the audio.

### Experimental Version
The experimental version:
1. Searches YouTube for the song
2. Uses Google's Gemini AI to analyze the video and detect music timestamps
3. Downloads the full audio
4. Trims the audio to only include the musical content
5. Saves the trimmed version as an MP3 file
6. Cleans up temporary files

<br>


## Experimantal Version Roadmap
1. Gemini isn't reliable when attaching youtube video
    - Will try uploading the audio instead of YT Video.
    - Or use another approach based on above method's performance.

## Upcoming Features
1. Batch Download
2. Thumbnail & Metadata (Optional, via parameters)
3. Support for Sptofiy as source alongside YT