"""
Music Downloader
---------------
A simple program to download MP3 files from YouTube by searching for song names.
Uses pytubefix for downloading and youtube_search for searching videos.
"""
from pytubefix import YouTube
from youtube_search import YoutubeSearch

def get_song_url(song_name):

    """
    Search YouTube for a song and return the URL of the first result.
    
    Args:
        song_name (str): The name of the song to search for
        
    Returns:
        str: Complete YouTube URL for the first search result
    """

    results = YoutubeSearch(song_name, max_results=1).to_dict()
    return "youtube.com" + results[0]['url_suffix']

def mp3_down(url, filename):

    """
    Download audio from a YouTube URL and save it as an MP3 file.
    
    Args:
        url (str): YouTube URL to download from
        filename (str): Output filename for the MP3 file
    """

    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True, abr='128kbps').first()
    audio_stream.download(filename=filename)

def main(song_name: str):

    """
    Main function to search for a song and download it as MP3.
    
    Args:
        song_name (str): Name of the song to search for and download
    """
    filename = song_name + ".mp3"
    song_url = get_song_url(song_name)
    mp3_down(song_url, filename)
    
# Example usage: Download "Rangapura vihara agam"
main("Rangapura vihara agam")