import yt_dlp

def download_video(url):
    """
    Download a YouTube video using the yt-dlp library.

    Args:
        url (str): The URL of the YouTube video to download
    """
    ydl_opts = {
        'format': 'best',
        # 'format': 'best'/'bestaudio',   # Download the best quality video/audio
        'outtmpl': '%(title)s.%(ext)s',  # Save the file with the video title as the filename
        'noplaylist': True,              # Only download a single video, not a playlist
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
