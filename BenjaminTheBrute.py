#send post request to the server
#host = "https://bondogge.com/createPost"
#header data for the post request
#userID = 24
#sessID = number that increments by 1 each time until it is successful

import requests

host = "https://bondogge.com/createPost"
userID = 24
sessID = 1

while True:
    #make a post request to the server
    response = requests.post(host, data={'userID': userID, 'sessID': sessID})
    #read the response
    data = response.text
    #print the response
    if "Error:" in data:
        print("Fail" + str(sessID))
        sessID += 1
    else:
        print(data)
        break