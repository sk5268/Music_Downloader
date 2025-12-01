from moviepy import VideoFileClip

video = VideoFileClip("")
trimmed_video = video.subclipped(119, 133)
trimmed_video.write_videofile("", audio_codec="aac")