#magic bytes for png
png = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
import os
the_png = ""
#read the first 8 bytes of the files located at /tmp
def is_png_bytes(folder):
    #get a list of files in /tmp
    files = os.listdir(folder)
    #loop through the files
    for file in files:
        #open the file
        with open("/tmp/" + file, "rb") as f:
            #read the first 8 bytes
            bytes = f.read(8)
            #check if the bytes are equal to the png magic bytes
            if bytes == png:
                #save the filename to the variable the_png
                the_png = file
                #read the file
                contents = f.read()
                print(contents)
                return the_png, contents
    #return None if no file is found
    return "no png found"

is_png_bytes("/tmp")