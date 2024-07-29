import yt_dlp
# This program is untested

# Downloading a video segment requires ffmpeg to be installed
# brew install ffmpeg

import yt_dlp

def download_video_segment(url, start_time, end_time):
    """
    Download a YouTube video using the yt-dlp library.

    Args:
        url (str): The URL of the YouTube video to download
        start_time (str): The start time of the video segment to download
        end_time (str): The end time of the video segment to download
    """
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferredcodec': 'mp4',
        }, {
            'key': 'FFmpegTrim',
            'trim_start': start_time,
            'trim_end': end_time,
        }],
        'ffmpeg_location': '/usr/local/bin/ffmpeg',  # Specify the path to ffmpeg if not in PATH
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download and trimming of the segment completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    start_time = "00:00:00"  # Start time in hh:mm:ss or mm:ss
    end_time = "00:02:44"    # End time in hh:mm:ss or mm:ss
    download_video_segment(video_url, start_time, end_time)
