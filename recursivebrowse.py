#we need to recursively browse the directories and subdirectories to find the file
#return the filename of the file found

import os


def recursivebrowse(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file:
                return file
    return None

print(recursivebrowse("/tmp"))