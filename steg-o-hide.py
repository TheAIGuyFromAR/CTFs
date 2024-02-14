#
# Hide text in the image /tmp/image.gif
# Append the word alieneye to end of the file.
import os

#open the file

with open("/tmp/image.gif", "ab") as file:
    file.write(b"alieneye")
    file.close()
    print("done")
    