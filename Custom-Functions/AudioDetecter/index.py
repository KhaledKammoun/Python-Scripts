import os
import numpy as np
import librosa
import moviepy.editor as mp

# Function to extract audio from the video
def extract_audio_from_video(video_file, output_audio_file):
    video = mp.VideoFileClip(video_file)
    video.audio.write_audiofile(output_audio_file)

# Function to find matching audio segments using cross-correlation
def find_audio_matches(long_audio, sample_audio, sr, threshold=0.5):
    # Cross-correlate the audio signals
    correlation = np.correlate(long_audio, sample_audio, mode='valid')
    
    # Normalize the correlation
    correlation = correlation / (np.linalg.norm(long_audio) * np.linalg.norm(sample_audio))
    
    # Find the matching segments where the correlation exceeds the threshold
    matches = np.where(correlation > threshold)[0]
    
    return matches

# Function to remove matching video segments
def remove_video_segments(video_file, matches, sample_duration, sr, output_file):
    video = mp.VideoFileClip(video_file)
    segments = []
    
    # Convert matches (audio indices) to video timestamps
    for match in matches:
        start_time = match / sr  # Convert to seconds
        end_time = start_time + sample_duration
        
        # Add segments before and after the match to keep them
        if segments and start_time <= segments[-1][1]:
            segments[-1][1] = end_time  # Extend the last segment
        else:
            segments.append([start_time, end_time])
    
    # Create subclips for the remaining video
    final_clips = []
    prev_end = 0
    for segment in segments:
        start, end = segment
        if start > prev_end:
            final_clips.append(video.subclip(prev_end, start))
        prev_end = end
    
    if prev_end < video.duration:
        final_clips.append(video.subclip(prev_end, video.duration))
    
    # Concatenate the remaining video clips
    final_video = mp.concatenate_videoclips(final_clips)
    
    # Write the output video file
    final_video.write_videofile(output_file, codec="libx264")

# Main function to handle the whole process
def process_video_and_audio(video_file, audio_file, output_video_file):
    # Step 1: Extract audio from the long video
    long_audio_file = "temp_long_audio.wav"
    extract_audio_from_video(video_file, long_audio_file)
    
    # Step 2: Load both audios
    long_audio, sr = librosa.load(long_audio_file, sr=None)
    sample_audio, _ = librosa.load(audio_file, sr=sr)  # Match sampling rates
    
    # Step 3: Find the matching segments in the long video based on audio
    matches = find_audio_matches(long_audio, sample_audio, sr)
    
    # Step 4: Remove the matching video segments
    sample_duration = librosa.get_duration(sample_audio, sr=sr)
    remove_video_segments(video_file, matches, sample_duration, sr, output_video_file)
    
    # Clean up temporary audio file
    os.remove(long_audio_file)

# Usage example
if __name__ == "__main__":
    long_video_path = "long_video.mp4"
    audio_clip_path = "audio_clip.mp3"
    output_video_path = "output_video_without_repeats.mp4"
    
    process_video_and_audio(long_video_path, audio_clip_path, output_video_path)
