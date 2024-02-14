import os

# os.walk() returns a generator object
# that can be iterated through
# to get the names of files and folders
# in a directory tree
#
# The generator object is a tuple
# with three values:
# 1. The current directory name
# 2. A list of subdirectories in the current directory
# 3. A list of files in the current directory
#
# The generator object is recursive
# so it will return the directory tree
# in a depth-first order
#
# The generator object is lazy
# so it will only return the next directory
# when you ask for it
#
# The generator object is stateful
# so it remembers where it is up to
# in the directory tree
#
# The generator object is a one-shot iterator
# so once you have iterated through it
# it will be exhausted
#
# The generator object is not thread-safe
# so it should not be shared between threads
#
# The generator object is not re-entrant
# so it cannot be restarted
#
# The generator object is not pickleable
# so it cannot be saved to disk
#
# The generator object is not copyable
# so it cannot be copied
#
# The generator object is not seekable
# so it cannot be rewound

# The directory to start from
start_dir = '/tmp'

# The generator object
# that will return the directory tree
# in a depth-first order
dir_tree = os.walk(start_dir)

# Iterate through the generator object

# Get the next directory
# in the directory tree
# and print it out


#find the file in the /tmp/aliendir directory and oprint it out
def recursive_folder_search(dir_tree):
    for dir_name in dir_tree:
        if dir_name[0] == "/tmp/aliendir":
            print(dir_name)
            #list files in the directory
            print(dir_name[2])
            #print the file
            print(dir_name[2][0])
            #print the contents of the file
            with open("/tmp/aliendir/" + dir_name[2][0], "r") as file:
                data = file.read()
                print(data)
            break
        else:
            #look in the first folder in the directory
            recursive_folder_search()

recursive_folder_search(dir_tree)