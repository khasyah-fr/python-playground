import subprocess
import os
from yt_dlp import YoutubeDL

def download_youtube_video(url, output_path="downloaded_video.mp4"):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': output_path,
        'merge_output_format': 'mp4',
        'quiet': True,
        'no_warnings': True
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path

def cut_video(input_file, start_time, duration, output_file="cut_output.mp4", reencode=False):
    if reencode:
        cmd = [
            "ffmpeg", "-y", "-ss", start_time, "-i", input_file, "-t", duration,
            "-c:v", "libx264", "-c:a", "aac", "-strict", "experimental", output_file
        ]
    else:
        cmd = [
            "ffmpeg", "-y", "-ss", start_time, "-i", input_file, "-t", duration,
            "-c", "copy", output_file
        ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_file

youtube_url = "https://www.youtube.com/watch?v=PPmQd2zWdP0"
start = "00:01:00"
duration = "00:00:30"

downloaded = download_youtube_video(youtube_url)
cut_video(downloaded, start, duration, output_file="final_clip.mp4", reencode=False)