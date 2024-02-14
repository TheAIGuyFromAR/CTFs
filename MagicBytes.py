MBpng = "0x89 0x50 0x4E 0x47 0x0D 0x0A 0x1A 0x0A"
MBjpg = "0xFF 0xD8 0xFF"
MBgif = "0x47 0x49 0x46 0x38 0x37 0x61"
MBbmp = "0x42 0x4D"
MBtiff = "0x49 0x49 0x2A 0x00"


#imports
import os

#look at the first 8 bytes of the file
#compare the first 8 bytes to the magic bytes
#return the file type


filelist = []
def get_file_type(file):
    #open the file
    with open(file, "rb") as file:
        #read the first 8 bytes
        data = file.read(8)
        #split the data into a list
        data = data.split()
        #print(data)
        #compare the first 8 bytes to the magic bytes
        if data == MBpng.split():
            print("PNG")
            return "PNG"
        elif data == MBjpg.split():
            print("JPG")
            return "JPG"
        elif data == MBgif.split():
            print("GIF")
            return "GIF"
        elif data == MBbmp.split():
            print("BMP")
            return "BMP"
        elif data == MBtiff.split():
            print("TIFF")
            return "TIFF"
        else:
            print("Unknown File Type")
            return "Unknown File Type"

#make list of all files in folder
def list_files(startpath,filelist):
    #make a list of all files in the current directory
    files = os.listdir(startpath)
    #print(files)
    #loop through the list of files
    for file in files:
        #get the file type
        filelist = filelist.append(get_file_type(file))

startpath = "/tmp"
list_files(startpath,filelist)
print(filelist)
