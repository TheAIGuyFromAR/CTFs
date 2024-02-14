#list all files in /tmp

import os

files = os.listdir("/tmp")
#print first 8 bytes of each file
def MBcheck(files):
  for file in files:
      with open("/tmp/" + file, "rb") as file1:
        data = file1.read(8)
      	  #compare the first 8 bytes to the magic bytes for png
        if data == b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A":
            print(file, "PNG")
            return file
        
TheFile = MBcheck(files)
print(TheFile)
with open(f"/tmp/{TheFile}", "r") as f:
  txt = f.read().encode('utf-8')
  print(txt)