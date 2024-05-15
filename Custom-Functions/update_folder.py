import os
import shutil
import hashlib
import filecmp
import sys 
def calculate_directory_hash(directory):
    """Calculate a hash of the directory contents."""
    total_bytes = 0
    processed_bytes = 0
    hasher = hashlib.sha256()

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_bytes += os.path.getsize(file_path)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as file_contents:
                while True:
                    data = file_contents.read(65536)  # Read in 64k chunks
                    if not data:
                        break
                    hasher.update(data)
                    processed_bytes += len(data)
                    progress = int((processed_bytes / total_bytes) * 50)  # 50 characters for the progress bar
                    sys.stdout.write("\r[" + "=" * progress + " " * (50 - progress) + f"] {progress * 2}%")
                    sys.stdout.flush()

    sys.stdout.write("\n")
    return hasher.hexdigest()

def are_folders_identical(folder1, folder2):
    print(f"Calculating hash for {folder1}...")
    hash1 = calculate_directory_hash(folder1)
    print(f"Hash for {folder1}: {hash1}")

    print(f"Calculating hash for {folder2}...")
    hash2 = calculate_directory_hash(folder2)
    print(f"Hash for {folder2}: {hash2}")

    if hash1 == hash2:
        return True
    else:
        return False
def update_folder(source_dir, destination_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            
            source_file = os.path.join(root, file)
            dest_file = os.path.join(destination_dir, os.path.relpath(source_file, source_dir))

            # Ensure the destination directory for the file exists
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)

            # Check if the file exists in the destination
            if not os.path.exists(dest_file) or \
               (os.path.exists(dest_file) and os.path.getmtime(source_file) > os.path.getmtime(dest_file)):
                # Copy the file if it's new or modified
                shutil.copy2(source_file, dest_file)
                print(f"Copied: {source_file} -> {dest_file}")

    # Remove files in the destination that no longer exist in the source
    for root, _, files in os.walk(destination_dir):
        for file in files:
            dest_file = os.path.join(root, file)
            source_file = os.path.join(source_dir, os.path.relpath(dest_file, destination_dir))

            if not os.path.exists(source_file):
                # Remove the file if it doesn't exist in the source
                os.remove(dest_file)
                print(f"Removed: {dest_file}")
if __name__ == "__main__":
    
    source_directory = "~/Desktop/Python"
    destination_directory = "~/Python"
    update_folder(source_directory, destination_directory)
    """
    if are_folders_identical(source_directory, destination_directory):
        print("The two folders are identical.")
    else:
        print("The two folders are not identical.")
    """