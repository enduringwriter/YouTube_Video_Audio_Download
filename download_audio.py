import yt_dlp
# This program is untested

# Downloading an audio segment requires ffmpeg to be installed
# brew install ffmpeg

def download_audio(url):
    """ Download an audio segment from a YouTube video using the yt-dlp library.

    Args:
        url (str): The URL of the YouTube video to download
    """
    ydl_opts = {
        'format': 'bestaudio/best',  # Select the best audio format available
        'outtmpl': '%(title)s.%(ext)s',  # Save the file with the video title as the filename
        'noplaylist': True,              # Only download a single video, not a playlist
        'postprocessors': [{  # Convert the audio to mp3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_audio(video_url)
