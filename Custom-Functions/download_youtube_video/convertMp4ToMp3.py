from moviepy.editor import VideoFileClip

def convert_video_to_audio(video_path, audio_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Extract audio from the video
    audio_clip = video_clip.audio

    # Write the audio to an MP3 file
    audio_clip.write_audiofile(audio_path, codec='mp3')

    # Close the audio clip
    audio_clip.close()

if __name__ == "__main__":
    # Replace 'input_video.mp4' with the path to your input video
    input_video_path = 'C:/Users/khale/Downloads/ABC/video.mp4'

    # Replace 'output_audio.mp3' with the desired path for the output audio file
    output_audio_path = 'C:/Users/khale/Downloads/ABC/video.mp3'

    convert_video_to_audio(input_video_path, output_audio_path)
