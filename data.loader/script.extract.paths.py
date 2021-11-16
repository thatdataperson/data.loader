import os
import csv

baseDirectory = 'C:/'
# We need an array for the directories
directories = []

# Grab a copy of the full paths of the files and directories to process
filesOrDirectories = os.listdir(baseDirectory)
filesOrDirectoriesPaths = map(lambda name: os.path.join(baseDirectory, name), filesOrDirectories)

# For each object, only store it if it's a directory
for file in filesOrDirectoriesPaths:
    if os.path.isdir(file): directories.append(file)

# Output the list of directories to a csv for processing
with open('C:/data/data.list.directories.csv', 'w', newline= '') as f:
    write = csv.writer(f)
    write.writerow(['Directory'])
    for item in directories:
        write.writerow([item])