from flask import Flask, render_template, request
from pytube import YouTube, Playlist
import os

app = Flask(__name__)

def download_playlist(playlist_url, output_path='~/Downloads'):
    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)
        # Create a folder for the playlist
        playlist_folder = os.path.join(output_path, playlist.title.replace(' ','_'))
        os.makedirs(playlist_folder, exist_ok=True)

        # Print playlist details
        print(f"Downloading playlist: {playlist.title}")

        # Iterate through each video in the playlist and download it
        i = 1
        for video_url in playlist.video_urls:
            print("Video {} :\n".format(i))
            download_video(video_url, playlist_folder)
            i += 1

        print("Playlist Download complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

def download_video(video_url, resolution='1080p', output_path='~/Downloads'):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Find a stream with the specified resolution
        
        video_stream = yt.streams.get_highest_resolution()
        if video_stream:
            # Print video details
            print(f"Downloading: {yt.title}")
            print(f"Resolution: {video_stream.resolution}")

            video_stream.download(output_path)
            print("Download complete!")
        else:
            print(f"No {resolution} stream available for {yt.title}")

    except Exception as e:
        print(f"An error occurred: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        output_path = request.form['output_path']
        desition = int(request.form['desition'])
        if desition == 1:
            playlist_url = request.form['playlist_url']
            download_playlist(playlist_url, output_path)
        elif desition == 2:
            video_url = request.form['video_url']
            download_video(video_url, "1080p", output_path)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
