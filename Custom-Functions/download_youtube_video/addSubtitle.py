import os
import urllib.request
import json


from moviepy.editor import TextClip, CompositeVideoClip, concatenate_videoclips,VideoFileClip, ColorClip
import numpy as np
import ffmpeg

from base64 import b64encode
from faster_whisper import WhisperModel

from ipywidgets import widgets
from IPython.display import display, HTML, YouTubeVideo, Audio


# Step 1: Download video or upload the video in mp4 format
mp4videoURL = "C://Users/khale/Downloads/ABC/video.mp4"  # Replace with your video URL
videofilename = mp4videoURL.split('/')[-1]

urllib.request.urlretrieve(mp4videoURL, videofilename)

audiofilename = videofilename.replace(".mp4",'.mp3')

# Create the ffmpeg input stream
input_stream = ffmpeg.input(videofilename)

# Extract the audio stream from the input stream
audio = input_stream.audio

# Save the audio stream as an MP3 file
output_stream = ffmpeg.output(audio, audiofilename)

# Overwrite output file if it already exists
output_stream = ffmpeg.overwrite_output(output_stream)

ffmpeg.run(output_stream)

Audio(audiofilename)

model_size = "medium"
model = WhisperModel(model_size)
segments, info = model.transcribe(audiofilename, word_timestamps=True)
segments = list(segments)  # The transcription will actually run here.
for segment in segments:
    for word in segment.words:
        print("[%.2fs -> %.2fs] %s" % (word.start, word.end, word.word))

wordlevel_info = []

for segment in segments:
    for word in segment.words:
      wordlevel_info.append({'word':word.word,'start':word.start,'end':word.end})

# Create a table to display the wordlevel_info
table_columns = ['Start', 'End', 'Word']
# Create the table rows
table_rows = []

for word_info in wordlevel_info:
    start_widget = widgets.Text(value=str(word_info['start']))
    end_widget = widgets.Text(value=str(word_info['end']))
    word_widget = widgets.Text(value=word_info['word'])
    row_widgets = widgets.HBox([start_widget, end_widget, word_widget])
    table_rows.append(row_widgets)


# Create the update button
button = widgets.Button(description='Update')

# Create the output area for displaying the updated wordlevel_info
output_area = widgets.Output()

# Create a new variable to store the modified wordlevel_info
modified_wordlevel_info = []

def update_wordlevel_info(event):
    with output_area:
        output_area.clear_output()
        updated_wordlevel_info = []

        for row_widgets in table_rows:
            start = float(row_widgets.children[0].value)  # Convert start to float
            end = float(row_widgets.children[1].value)  # Convert end to float
            word = row_widgets.children[2].value
            word = word.strip()
            updated_wordlevel_info.append({'start': start, 'end': end, 'word': word})

        # Print the updated wordlevel_info
        print(updated_wordlevel_info)

        # Assign updated_wordlevel_info to modified_wordlevel_info
        global modified_wordlevel_info
        modified_wordlevel_info = updated_wordlevel_info

button.on_click(update_wordlevel_info)

# Create the table widget
table_widget = widgets.VBox(table_rows)

# Display the UI elements
display(table_widget, button, output_area)

with open('data.json', 'w') as f:
    json.dump(modified_wordlevel_info, f,indent=4)

with open('data.json', 'r') as f:
    wordlevel_info_modified = json.load(f)

def split_text_into_lines(data):

    MaxChars = 30
    #maxduration in seconds
    MaxDuration = 2.5
    #Split if nothing is spoken (gap) for these many seconds
    MaxGap = 1.5

    subtitles = []
    line = []
    line_duration = 0
    line_chars = 0


    for idx,word_data in enumerate(data):
        word = word_data["word"]
        start = word_data["start"]
        end = word_data["end"]

        line.append(word_data)
        line_duration += end - start

        temp = " ".join(item["word"] for item in line)


        # Check if adding a new word exceeds the maximum character count or duration
        new_line_chars = len(temp)

        duration_exceeded = line_duration > MaxDuration
        chars_exceeded = new_line_chars > MaxChars
        if idx>0:
          gap = word_data['start'] - data[idx-1]['end']
          # print (word,start,end,gap)
          maxgap_exceeded = gap > MaxGap
        else:
          maxgap_exceeded = False


        if duration_exceeded or chars_exceeded or maxgap_exceeded:
            if line:
                subtitle_line = {
                    "word": " ".join(item["word"] for item in line),
                    "start": line[0]["start"],
                    "end": line[-1]["end"],
                    "textcontents": line
                }
                subtitles.append(subtitle_line)
                line = []
                line_duration = 0
                line_chars = 0


    if line:
        subtitle_line = {
            "word": " ".join(item["word"] for item in line),
            "start": line[0]["start"],
            "end": line[-1]["end"],
            "textcontents": line
        }
        subtitles.append(subtitle_line)

    return subtitles
     
linelevel_subtitles = split_text_into_lines(wordlevel_info_modified)

for line in linelevel_subtitles:
  json_str = json.dumps(line, indent=4)

def create_caption(textJSON, framesize,font = "Helvetica",color='white', highlight_color='yellow',stroke_color='black',stroke_width=1.5):
    wordcount = len(textJSON['textcontents'])
    full_duration = textJSON['end']-textJSON['start']

    word_clips = []
    xy_textclips_positions =[]

    x_pos = 0
    y_pos = 0
    line_width = 0  # Total width of words in the current line
    frame_width = framesize[0]
    frame_height = framesize[1]

    x_buffer = frame_width*1/10

    max_line_width = frame_width - 2 * (x_buffer)

    fontsize = int(frame_height * 0.075) #7.5 percent of video height

    space_width = ""
    space_height = ""

    for index,wordJSON in enumerate(textJSON['textcontents']):
      duration = wordJSON['end']-wordJSON['start']
      word_clip = TextClip(wordJSON['word'], font = font,fontsize=fontsize, color=color,stroke_color=stroke_color,stroke_width=stroke_width).set_start(textJSON['start']).set_duration(full_duration)
      word_clip_space = TextClip(" ", font = font,fontsize=fontsize, color=color).set_start(textJSON['start']).set_duration(full_duration)
      word_width, word_height = word_clip.size
      space_width,space_height = word_clip_space.size
      if line_width + word_width+ space_width <= max_line_width:
            # Store info of each word_clip created
            xy_textclips_positions.append({
                "x_pos":x_pos,
                "y_pos": y_pos,
                "width" : word_width,
                "height" : word_height,
                "word": wordJSON['word'],
                "start": wordJSON['start'],
                "end": wordJSON['end'],
                "duration": duration
            })

            word_clip = word_clip.set_position((x_pos, y_pos))
            word_clip_space = word_clip_space.set_position((x_pos+ word_width, y_pos))

            x_pos = x_pos + word_width+ space_width
            line_width = line_width+ word_width + space_width
      else:
            # Move to the next line
            x_pos = 0
            y_pos = y_pos+ word_height+10
            line_width = word_width + space_width

            # Store info of each word_clip created
            xy_textclips_positions.append({
                "x_pos":x_pos,
                "y_pos": y_pos,
                "width" : word_width,
                "height" : word_height,
                "word": wordJSON['word'],
                "start": wordJSON['start'],
                "end": wordJSON['end'],
                "duration": duration
            })

            word_clip = word_clip.set_position((x_pos, y_pos))
            word_clip_space = word_clip_space.set_position((x_pos+ word_width , y_pos))
            x_pos = word_width + space_width


      word_clips.append(word_clip)
      word_clips.append(word_clip_space)


    for highlight_word in xy_textclips_positions:

      word_clip_highlight = TextClip(highlight_word['word'], font = font,fontsize=fontsize, color=highlight_color,stroke_color=stroke_color,stroke_width=stroke_width).set_start(highlight_word['start']).set_duration(highlight_word['duration'])
      word_clip_highlight = word_clip_highlight.set_position((highlight_word['x_pos'], highlight_word['y_pos']))
      word_clips.append(word_clip_highlight)

    return word_clips,xy_textclips_positions

input_video = VideoFileClip(videofilename)
frame_size = input_video.size

all_linelevel_splits=[]

for line in linelevel_subtitles:
  out_clips,positions = create_caption(line,frame_size)

  max_width = 0
  max_height = 0

  for position in positions:
    # print (out_clip.pos)
    # break
    x_pos, y_pos = position['x_pos'],position['y_pos']
    width, height = position['width'],position['height']

    max_width = max(max_width, x_pos + width)
    max_height = max(max_height, y_pos + height)

  color_clip = ColorClip(size=(int(max_width*1.1), int(max_height*1.1)),
                       color=(64, 64, 64))
  color_clip = color_clip.set_opacity(.6)
  color_clip = color_clip.set_start(line['start']).set_duration(line['end']-line['start'])

  # centered_clips = [each.set_position('center') for each in out_clips]

  clip_to_overlay = CompositeVideoClip([color_clip]+ out_clips)
  clip_to_overlay = clip_to_overlay.set_position("bottom")


  all_linelevel_splits.append(clip_to_overlay)

input_video_duration = input_video.duration


final_video = CompositeVideoClip([input_video] + all_linelevel_splits)

# Set the audio of the final video to be the same as the input video
final_video = final_video.set_audio(input_video.audio)

# Save the final clip as a video file with the audio included
final_video.write_videofile("output.mp4", fps=24, codec="libx264", audio_codec="aac")

mp4 = open("output.mp4",'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""

""" % data_url)

# Create a dummy TextClip object
dummy_clip = TextClip('Dummy Text')

# Get the available fonts
available_fonts = dummy_clip.list('font')

# Print the available fonts
for font in available_fonts:
    print(font)