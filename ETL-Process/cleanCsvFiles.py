
# Clean the CSV files, to put them seperated also by semicolons
# Exemple : 
# "1,James,Smith,""123 Main St, Springfield, IL"",jsmith1@customer.com,555-190-3233"
#  to ==> 
# 1;James;Smith;"123 Main St, Springfield, IL";jsmith1@customer.com;555-190-3233

import csv
import os

def clean_csv_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".csv"):
                filename, extension = os.path.splitext(file)
                with open(os.path.join(root, file), 'r') as f:
                    reader = csv.reader(f)
                    with open(os.path.join(root, filename+"_clean"+extension), 'w') as fo:
                        writer = csv.writer(fo, delimiter=';')
                        writer.writerows(reader)


def clean_folder(path) :
    for root, dirs, files in os.walk(path):
        for file in files:
            if not "_clean" in file:
                os.remove(os.path.join(root, file))
    



def clean_filesName(path) : 
    i = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if "_clean" in file:
                filename, extension = os.path.splitext(file)
                if filename == "_clean":
                    new_filename = f"File {i + 1}"
                else:
                    new_filename = filename.replace("_clean", "")
                i += 1
                try:
                    os.rename(os.path.join(root, file), os.path.join(root, new_filename+extension))
                except PermissionError:
                    print(f"The file {file} is being used by another process. Can't rename it.")
                

 
filePath = "path\\to\\your\\csv\\files"
clean_filesName(filePath)