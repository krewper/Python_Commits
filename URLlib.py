import urllib.request
import urllib.parse

try:
    x = urllib.request.urlopen('https:www.google.com')
    print(x.read())
    
except Exception as e :
    print(str(e))
    
    