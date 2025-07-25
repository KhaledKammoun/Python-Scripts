from spleeter.separator import Separator

# Initialize Spleeter with 4 stems model (vocal, drums, bass, others)
separator = Separator('spleeter:4stems')

# Separate the audio file

path_1 = "path/to/Input/1.mp3"
path_2 = "path/to/Output"

separator.separate_to_file(path_1, path_2)
