import csv

csv_file_path = "data.csv"  # Replace with the path to your CSV file

# Read CSV file into a list of dictionaries
csv_data = []
with open(csv_file_path, "r") as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        csv_data.append(row)
        print(row)

# Print the data as dictionaries
for row in csv_data:
    print(row)
