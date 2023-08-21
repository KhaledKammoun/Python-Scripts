import zipfile

zip_file_path = "example.zip"  # Replace with the path to your zip file

# Open the zip archive
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract all files to a target directory
    zip_ref.extractall("target_directory")  # Replace with your target directory path
