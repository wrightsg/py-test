import csv

file_name = "test.csv"

# Open file
with open(file_name, "r") as csv_file:
    # Get file reader (?)
    reader = csv.reader(csv_file)
    # Create empty list
    csv_list = []
    # Put rows of file into list
    for row in reader:
        csv_list = csv_list + [row]

# Print the list
print(csv_list)

