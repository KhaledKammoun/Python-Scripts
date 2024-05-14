from flask import Flask, render_template, request
from pytube import YouTube, Playlist
import os
import shutil
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

def download_playlist(playlist_url, output_path='~/Downloads'):
    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)
        # Create a folder for the playlist
        playlist_folder = output_path + '/' + playlist.title.replace(' ','_')
        os.makedirs(playlist_folder, exist_ok=True)

        # Print playlist details
        print(f"Downloading playlist: {playlist.title}")

        # Iterate through each video in the playlist and download it
        i = 1
        for video_url in playlist.video_urls:
            print("Video {} :\n".format(i))
            
            download_video(video_url, playlist_folder, str(i))
            i += 1

        print("Playlist Download complete!")

    except Exception as e:
        print(f"An error occurred while downloading playlist: {playlist.title}")
        print(f"Error details: {e}")

def concat_video_audio(output_path, video_audio_path, title):
    video = VideoFileClip(video_audio_path + "/video.mp4")
    audio = AudioFileClip(video_audio_path + "/audio.mp3")
    final_clip = video.set_audio(audio)
    output_file_path = output_path + "/" + title + ".mp4"
    final_clip.write_videofile(output_file_path)


def download_video(video_url, output_path='~/Downloads', name="1", target_resolution="480p"):
    try:
        

        # Create a YouTube object
        yt = YouTube(video_url)
        # video_stream = yt.streams.get_highest_resolution()
        video_stream = None
        # print(yt.streams)
        for stream in yt.streams:
            if stream.resolution == target_resolution and stream.mime_type == "video/mp4":
                video_stream = stream
                break

        if (video_stream == None) : 
            # Get the highest resolution stream
            stream = yt.streams.get_highest_resolution()
            # print("1080p quality not exist !!!")
            
            print(f"Downloading: {yt.title}")
            print(f"Resolution: {stream.resolution}")

            # Download the video to the current directory
            stream.download(output_path, name)
            print("Download complete!")
        else :
            # print(video_stream)
            # print("111")            
            new_folder = "/New_Folder"
            # create a new  folder
            video_path = output_path + new_folder
            print("Video Path : ", video_path)
            os.makedirs(video_path, exist_ok=True)

            audio_stream = yt.streams.get_audio_only()
            if video_stream and audio_stream:
                # Print video details
                print(f"Downloading: {yt.title}")
                print(f"Resolution: {video_stream.resolution}")

                # Download the video
                video_stream.download(video_path, "video.mp4")
                # Download the audio
                audio_stream.download(video_path, "audio.mp3")

                # Concat video and audio
                concat_video_audio(output_path, video_path, name)
                print("Download complete!")
            else:
                print(f"No video stream available for {yt.title}")

        if 'video_path' in locals():
            shutil.rmtree(video_path)

    except Exception as e:
        print(f"An error occurred: {e}")

def index():

    while True : 
        print("-----------------------------------------------")
        print("-------------- YOUTUBE DOWNLOADER -------------")
        print("-------    POWERED BY KHALED KAMMOUN    -------")
        print("-----------------------------------------------")
        output_path = input("--- Download Path : ")
        print("--- SELECT ---")
        print("----- 1 : Download Playlist")
        print("----- 2 : Download Video")
        print("----- 3 : Download Custom Playlist")
        desition = int(input("--- TYPE 1, 2 or 3 : "))

        if desition in [1, 2] :
            string_var = "Playlist" if desition == 1 else "Video"
            url = input(f"--- {string_var} url : ")
        else :
            url_list = []
            url_var = ""
            
            while url_var.lower() != "q" :
                url_var = input(f"--- Video {len(url_list) + 1} : ")
                url_list.append(url_var)

        if desition == 1:
            download_playlist(url, output_path)
        elif desition == 2:
            target_resolution = "480p"
            download_video(url, output_path, target_resolution)
        

        stop_condition = input("--- Press q to quit : ") 
        if stop_condition == 'q' : 
            break

index()