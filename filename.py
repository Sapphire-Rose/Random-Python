# Imports
import os # Needed to create directory
import csv # Needed for CSV stuff

# Prompt user for directory
dir = input("Enter thine name of our working directory: ")

# Prompt user for filename to save stuff as
filename = input("Enter thine filename you want to write to: ")
# Construct path with directory and filename
path = dir + "/" + filename

# If directory doesn't exist, create it
os.makedirs(dir, exist_ok=True)

# Prompt user for name, address, and phone number
name = input("What ist thou nameth: ")
addy = input("Whereth do you dwell: ")
digits = input("Whatith be your digits: ")
info = [name, addy, digits]

# Write that info to directory/file.csv as CSV
file = open(path, 'w', newline='') # Open in write mode
writer = csv.writer(file) # Create writer thing
writer.writerow(info) # Write info to file
file.close() # Close file

# Read the file and print the values
with open(path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)
