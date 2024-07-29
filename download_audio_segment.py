import yt_dlp
# This program is untested

# Downloading an audio segment requires ffmpeg to be installed
# brew install ffmpeg

def download_audio(url, start_time, end_time):
    """ Download an audio segment from a YouTube video using the yt-dlp library

    Args:
        url (str): The URL of the YouTube video to download
        start_time (str): The start time of the audio segment to download
        end_time (str): The end time of the audio segment to download
    """
    ydl_opts = {
        'format': 'bestaudio/best',  # Select the best audio format available
        'outtmpl': '%(title)s.%(ext)s',  # Save the file with the video title as the filename
        'noplaylist': True,              # Only download a single video, not a playlist
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }, {
            'key': 'FFmpegVideoConvertor',
            'preferredcodec': 'mp3',
            'postprocessor_args': [
                '-ss', start_time,
                '-to', end_time
            ],
        }],
        'ffmpeg_location': '/path/to/ffmpeg',  # Specify the path to ffmpeg if not in PATH
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download and trimming completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    start_time = "00:00:00"  # Start time in hh:mm:ss
    end_time = "00:02:44"    # End time in hh:mm:ss
    download_audio(video_url, start_time, end_time)
