from pytube import YouTube,Playlist
import os
def download_playlist(playlist_url, output_path='~/Downloads'):
    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)
        # Create a folder for the playlist
        playlist_folder = os.path.join(output_path, playlist.title)
        os.makedirs(playlist_folder, exist_ok=True)

        # Print playlist details
        print(f"Downloading playlist: {playlist.title}")

        # Iterate through each video in the playlist and download it
        i = 1
        for video_url in playlist.video_urls:
            print("Video {} :\n".format(i))
            download_video(video_url, playlist_folder)
            i+=1

        print("Playlist Download complete!")

    except Exception as e:
        print(f"An error occurred: {e}")


def download_video(video_url, output_path='~/Downloads'):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        video_stream = yt.streams.get_highest_resolution()

        
        # Print video details
        print(f"Downloading: {yt.title}")
        print(f"Resolution: {video_stream.resolution}")

        video_stream.download(output_path)
        print("Download complete!")
        

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    output_path = input("Enter The Download Path : ")
    desition = int(input("Press 1 To Download A PlayList | Press 2 To Download A Video : "))
    if desition == 1 :
        playlist_url = input("Enter The PlayList URL : ")
        download_playlist(playlist_url, output_path)
    elif desition == 2 :
        video_url = input("Enter The Video URL : ")
        download_video(video_url, output_path)
