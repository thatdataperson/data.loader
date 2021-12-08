import os
import csv

# Let's create a function that:
#   accepts the following parameters:
#       a base directory string
#       a recursion level to say how deep we can search through the directory structure
#   runs through the base directory and generates an list of directories held within
#   passes back a list once complete

#Let's define a new class to store our directory objects
class directory:
    def __init__(self, directoryPath, accessibility):
        self.directoryPath = directoryPath
        self.accessibility = accessibility

def getDirectories(baseDirectory, recursionLevel):
    """
    This function generates a list of directories.
    It also returns some useful information about each directory.
    """

    # We need a list for the directories
    directories = []

    # We also need to keep in mind how deep down the rabbit hole we are allowed to go
    recursionLevel -= 1

    # For each object, only store it if it's a directory
    for entry in os.scandir(baseDirectory):
        if entry.is_dir():
            # Replace the directory path backslash with a forward slash
            directoryPath = entry.path.replace('\\', '/')
            # If we've found a directory, store it and assume it's accessible for now
            directories.append(directory(directoryPath, 'accessible'))
            # Try to open the directory if we're not at the end of our recursion yet
            if recursionLevel > 0:
                try:
                    directories = directories + getDirectories(directoryPath, recursionLevel)
                except PermissionError as e:
                    # If we can't gain access, store that fact
                    directories[-1].accessible = 'inaccessible'
            else:
                # If we never try accessing, let's store that fact too because it could be important
                directories[-1].accessible = 'untested'

    return directories

# Output a list of directories to a csv for processing
directories = getDirectories('C:/', 2)

with open('C:/data/data.list.directories.csv', 'w', newline= '') as f:
    write = csv.writer(f)
    write.writerow(['directoryPath','accessibility'])
    for i in directories:
        write.writerow([i.directoryPath, i.accessibility])