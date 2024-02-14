# pip install pycryptodome
from Crypto.Cipher import AES
import base64
import string

BLOCK_SIZE = 32

PADDING = '}'

# Encrypted text to decrypt
encrypted = "xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo="

def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e)).decode('latin-1').rstrip(PADDING)

secret = ''
with open('wor.txt', 'r') as f:
    for secret in f:
        secret = secret.rstrip('\n')
        #print("Secret: "+secret)
        if secret[-1:] == "\n":
            print("Error, new line character at the end of the string. This will not match!")
        #elif len(bytes(secret, 'latin-1')) >= 32:
         #   print("Error, string too long. Must be less than 32 bytes.")
          #  continue
        else:
            # create a cipher object using the secret with mode 
            # convert variable names secret from string to bytes
            
            #try:
                c = AES.new((bytes(secret, 'latin-1')+ (b'\0' * (BLOCK_SIZE-len(bytes(secret, 'latin-1'))))), AES.MODE_ECB)
                decoded = decode_aes(c, encrypted)


                for i in decoded:
                    if i not in string.printable:
                        decoded = ''
                        break
                    else:
                        continue        
                if decoded != '':
                    print('Decoded: '+decoded+"\n")
                    break
           