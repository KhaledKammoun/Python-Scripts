import assemblyai as aai

aai.settings.api_key = "3019cd50a3b743d1a49729cb0b3b907e"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("C:/Users/khale/Downloads/ABC/video.mp3")
srt = transcript.export_subtitles_srt()

output_srt_path = 'subtitles.srt'

# Write subtitles to file
with open(output_srt_path, 'w') as f:
    f.write(srt)