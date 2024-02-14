import zipfile
import itertools
import time


# Main code starts here...
# The file name of the zip file.
zipfilename = "planz.zip"
# The first part of the password. We know this for sure!
first_half_password = 'Super'
# We don't know what characters they add afterwards...
# This is case sensitive!
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#make a for loop to iterate through all the possible passwords
#possible passwords are "Super" + 3 characters (a-z)

for c in itertools.product(alphabet, repeat=3):
    # The current password we are trying
    password = first_half_password + ''.join(c)
    # Open the zip file with the current password
    # If the password is wrong, this will throw a RuntimeError exception
    try:
        with zipfile.ZipFile(zipfilename, "w") as zf:
            zf.extractall(pwd=password.encode())
        # If we reach here, the password was found!
            print(f'The password is: {password}')
        # Exit the program
            break
    except RuntimeError:
        # Tell the user that the password was wrong
        print(f'Incorrect password: {password}')
        # Go to the next password in the list
        continue




# If no password was found by the end, let us know!
        
print('All passwords with 3 characters have been tried.')