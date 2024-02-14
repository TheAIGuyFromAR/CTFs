#
# Write a script that makes HTTP requests to the server
# http://127.0.0.1:8082/selfdestruct until the numbers match
# and read the response to get the flag.
# You can easily run out of execution time in this challenge.
# You will need to check the response and stop your attack
# once you see the flag.
#

import urllib.request as urllib

def main():
    url = "http://127.0.0.1:8082/selfdestruct"
    #make a request to the server
    response = urllib.urlopen(url)
    #read the response
    data = response.read()
    #print the response
    if "Fail:" in data.decode():
      print("Fail")
    else:
      print(data)
    

for i in range(1,100):
    main()