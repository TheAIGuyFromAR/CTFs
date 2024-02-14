#
# Write a script that can guess cookie values
# and send them to the url http://127.0.0.1:8082/cookiestore
# Read the response from the logged in cookie value to get the flag.
# The cookie name the aliens are using is alien_id
# we believe the id is a number between 1 and 75
#
# Note: The script can timeout. If this occurs try narrowing
# down your search
#
import urllib.request
import requests
# The URL for the API
url = "127.0.0.1:8082/cookiestore"
method = "GET"

#cookie name is alien_id
cookie = "alien_id"
#cookie value is a number between 1 and 75
cookie_value = 1

#read the cookie value from the response
def read_cookie_value(response):
    #split the response on the cookie name
    response = response.split(cookie)
    #split the response on the ;
    response = response[1].split(";")
    #split the response on the =
    response = response[0].split("=")
    #return the cookie value
    return response[1]

#read the response from the url
def read_response(url):
    #make a request to the url
    with urllib.request.urlopen(url) as response:
        #read the response
        the_page = response.read()
        #decode the response
        the_page = the_page.decode('utf-8')
        #return the response
        return the_page
    
print(read_response(url))