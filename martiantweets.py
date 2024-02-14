#
# The Tweet Bot API can be found at http://127.0.0.1:8082
#
# GET method sent to that URL:
# ...returns basic info about API
#
# POST method sent to that URL, with: \
#x-api-key:tweetbotkeyv1 in header

# - user=tweetbotuser in querystring
# - status-update=alientest in querystring
# ...creates a new social media post

import urllib.request
import time
import random
import string

# The URL for the API
url = "http://127.0.0.1:8082"
method = "GET"

# The API key

#make a post request with a custom header  x-api-key:{KEY} in header
# - user={USER} in querystring
# - status-update={TEXT} in querystring
# ...creates a new social media post
# The data we are going to send
data = {
    "user": "tweetbotuser",
    "status-update": "alientest"
}
headers = { 'x-api-key' : 'tweetbotkeyv1' }

# Encode the data
data = urllib.parse.urlencode(data)
# Encode the data to bytes
data = data.encode('ascii')
#add the headers to the request
req = urllib.request.Request(url, data, headers)
#make the request
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   print(the_page)






