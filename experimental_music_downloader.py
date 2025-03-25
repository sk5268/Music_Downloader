import os
from google import genai
from pytubefix import YouTube
from google.genai import types
from moviepy import AudioFileClip
from youtube_search import YoutubeSearch

def get_song_url(song_name):
    """
    Search YouTube for a song and return the URL of the first result.
    
    Args:
        song_name (str): The name of the song to search for.
        
    Returns:
        str: YouTube URL for the first search result.
    """
    
    results = YoutubeSearch(song_name, max_results=1).to_dict()
    return "youtube.com" + results[0]['url_suffix']

def audlen(url):
    """
    Analyze a YouTube video to identify when the music begins and ends.
    
    Uses Google's Gemini AI model to detect the timestamps where the actual
    musical content starts and ends in the video.
    
    Args:
        url (str): YouTube URL of the song.
        
    Returns:
        dict: Dictionary containing 'start' and 'end' timestamps in seconds.
    """
    
    client = genai.Client(
        api_key="",
    )

    model = "gemini-2.0-pro-exp-02-05"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=url,
                    mime_type="video/*",
                )
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0,
        top_p=0.95,
        top_k=64,
        max_output_tokens=8192,
        response_mime_type="application/json",
        system_instruction=[
            types.Part.from_text(text="""You are a specialized audio-video analysis assistant.
                                 Your task is to identify the precise timestamps where the actual musical content begins and ends in videos.
                                 
                                When provided with a video, analyze its content to determine:
                                1. The exact time (in seconds) when the main song/music begins
                                2. The exact time (in seconds) when the main song/music ends

                                IMPORTANT: Include ALL musical content as part of the song, including:
                                - Instrumental intros and outros
                                - Musical themes or background music that is part of the composition
                                - All verses, choruses, bridges, and musical interludes

                                Only exclude clearly non-musical segments such as:
                                - Spoken sponsor messages or advertisements
                                - Verbal introductions or commentary not accompanied by music
                                - End-screen calls to action without musical backing
                                - Silent credits or purely speech-based outros

                                Your response must be a valid JSON object with exactly two fields:
                                - "start": the timestamp in seconds when any musical content begins
                                - "end": the timestamp in seconds when all musical content ends

                                Example response:
                                {
                                "start": 12.5,
                                "end": 224.7
                                }

                                Be precise with your timestamps to the nearest 0.1 seconds if possible. 
                                If the video begins directly with music or ends with music, use 0 for start or the video's full duration for end, respectively."""
                                 ),
                                                    ],
    )

    resp =  client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    return eval(resp.text)

def mp3_down(url):
    """
    Download the audio from a YouTube video as an MP3 file.
    
    Args:
        url (str): YouTube URL of the song to download.
    """
    
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename="tmp.mp3")

def trim_audio(song_name, length: dict):
    """
    Trim the audio file according to the specified start and end times.
    
    Args:
        song_name (str): Name of the song (used for the output filename).
        length (dict): Dictionary containing 'start' and 'end' timestamps in seconds.
    """
    
    audio = AudioFileClip("tmp.mp3")
    trimmed_audio = audio.subclipped(length['start'], length['end'])
    trimmed_audio.write_audiofile(song_name+".mp3")

def cleanup():
    """
    Remove temporary files created during the download process.
    """
    
    try:
        os.remove("tmp.mp3")
    except:
        pass

def main(song_name: str):
    """
    Main function to download and trim a song from YouTube.
    
    This function coordinates the entire process of searching for the song,
    downloading it, analyzing its content, trimming it, and cleaning up.
    
    Args:
        song_name (str): The name of the song to download.
    """
    
    song_url = get_song_url(song_name)
    length = audlen(song_url)
    mp3_down(url=song_url)
    trim_audio(song_name, length)
    cleanup()
    

main("Rangapura Vihara Agam")