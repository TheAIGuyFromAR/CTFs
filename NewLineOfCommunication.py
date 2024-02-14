#We need you to write a script which can connect over TCP to the following server - localhost:10000
#send 'GET' to retrieve the encrypted messages. 
#then need to decrypt them and send them back split by \n. 
#you'll receive 3 sentences, and that they're encrypted with a caesar cipher with a different random offset per sentence.
#print the response after sending the decrypted messages to get the flag.

import socket
import string

def main():
    counter = 0
    host = 'localhost'
    port = 10000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    print("Connected to server")
    #send 
    s.send("GET".encode())
    data = s.recv(1024).decode()
    print("From server: " + str(data))
    #split the data into a list by newline character
    data = data.split("\n")
        #remove the first and last elements of the list
    data.pop(0)
    data.pop()
    print(data)
    cracked_messages = []
    for item in data:
      #decrypt each item in the list using the caesar cipher with a random offset
      result = ""
      #store in a variable named cracked_message + counter
      CrackTry = crack(item) 

      cracked_messages.append(CrackTry)



    #COmbine the three cracked messages into one string separated by newline characters
    print(cracked_messages)
    full_cracked_message = "\n".join(cracked_messages)
    #send the cracked message to the server
    s.send(full_cracked_message.encode())
    #recieve the message from the server
    data = s.recv(1024).decode()
    print("From server: " + str(data))
    #close connection
    s.close()


      

def crack(input):
    # Try an offset of every possibility from 0 to 25
    for i in range(0, 26):
        output = ""
        # For every character in the provided input
        for j in range(len(input)):
            char = input[j]
            # Move the character along by the offset
            if char != " ":
                newChar = chr((ord(char) + i - 65) % 26 + 65)
            else:
              newChar = char
            output += newChar
        if " THE " in output or " IN " in output or " ON " in output or " AN " in output or " TO " in output or " I " in output:        
          printer = "Combination " + str(i) + " = " + output
          print(printer)
          return output

if __name__ == '__main__':
    main()