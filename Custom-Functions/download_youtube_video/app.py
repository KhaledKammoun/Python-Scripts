from flask import Flask, render_template, request
from pytube import YouTube, Playlist
import os
import shutil, subprocess
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
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

def concat_video_audio(output_path, video_audio_path, title):
    video_file_path = os.path.join(video_audio_path, "video.mp4")
    audio_file_path = os.path.join(video_audio_path, "audio.mp3")
    output_file_path = os.path.join(output_path, title + ".mp4")

    # Run FFmpeg to mux audio and video
    cmd = f'ffmpeg -y -i "{video_file_path}" -i "{audio_file_path}" -filter:a aresample=async=1 -c:a flac -c:v copy "{output_file_path}"'
    
    try:
        subprocess.call(cmd, shell=True)
        print(f'Muxing Done: {output_file_path}')
    except Exception as e:
        print(f"An error occurred: {e}")

def download_video(video_url, output_path='~/Downloads', target_resolution = "1080p"):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        target_resolution = "480p"
        
        video_stream = None
        for stream in yt.streams :
            if stream.resolution == target_resolution and stream.mime_type =="video/mp4":
                video_stream = stream
                break
        
        
        new_folder = "/New_Folder"
        # create a new  folder
        # os.makedirs(output_path + new_folder)
        # Download first the video without audio
        video_path = output_path + new_folder
        
        
        audio_stream = yt.streams.get_audio_only()
        
        

        
        if video_stream and audio_stream:
            # Print video details
            print(f"Downloading: {yt.title}")
            print(f"Resolution: {video_stream.resolution}")

            # Download the video
            # video_stream.download(video_path, "video.mp4")
            # Download the audio
            # audio_stream.download(video_path,"audio.mp3")
            
            # Concat video and audio
            concat_video_audio(output_path, video_path, yt.title.replace(" ", "_"))

            # delete the new folder
            shutil.rmtree(output_path + new_folder)

            
            print("Download complete!")
        else:
            print(f"No video stream available for {yt.title}")

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
            target_resolution = "480p"
            download_video(video_url, output_path, target_resolution)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
