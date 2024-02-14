#You'll need to read the file and remove any characters that are not letters or numbers, then print out the remaining characters.

#There's a few ways you could accomplish this - perhaps Regex or using ASCII character values.

#The flag is the string you get after removing the non-alphanumeric characters.

#
# One of the agents has intercepted a file from the aliens
# The flag is hidden in large amount of non alphanumeric characters.
# The file lives at /tmp/destroymoonbase.gif
#

#open the file

#read the file

#remove the non-alphanumeric characters

#print the flag

#close the file

import os
import re

with open("/tmp/destroymoonbase.gif", "r") as file:
    data = file.read()
    #print(data)
    #print(re.sub(r'\W+', '', data))
    print(re.sub(r'\W+', '', data))
    file.close()

