#Unzip the file located at hives.zip and extract the files to /hives/ directory


import zipfile
import os

# make sure the /hives/ directory exists
if not os.path.exists("hives/"):
    os.makedirs("hives/")


#try all of the password in possiblepasswordlist to unzip the file and extract it to /tmp

possiblePasswordList = []
with open('TheWords.txt', 'r', encoding='latin-1') as f:
    for line in f:
        possiblePasswordList.append(line.strip())

for password in possiblePasswordList:
    try:
        with zipfile.ZipFile('hives.zip', 'r') as zf:
            zf.extractall(pwd=password.encode('latin-1'), path="hives/")
            print(f'The password is: {password}')
            break
    except RuntimeError:
        print(f'Incorrect password: {password}')
        continue




# If no password was found by the end, let us know!
print('All passwords have been tried.')