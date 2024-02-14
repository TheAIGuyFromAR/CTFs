# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp

import zipfile
import itertools

    
filename = '/tmp/alien-zip-2092.zip'
zFile = zipfile.ZipFile(filename)
alpha = "1234567890"
for i in itertools.product(alpha, repeat=3):
    password = ''.join(i)
    try:
        zFile.extractall(pwd=password.encode())
        print('Password found: ' + password)
        break
    except:
        pass
