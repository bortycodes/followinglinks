# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#html = urllib.request.urlopen(url, context=ctx).read()
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count = input('Enter count: ')
position = input('Enter position: ')

print('Retrieving: ', url)

i = 0
while( i < int(count)):
        i = i + 1
        pos = 0 
        # Retrieve all of the anchor tags
        tags = soup('a')
        for tag in tags:
            pos = pos + 1
            if(pos == int(position)):
                print('Retrieving: ', tag.get('href', None))
                html = urllib.request.urlopen(tag.get('href', None)).read()
                soup = BeautifulSoup(html, 'html.parser')

#C:\Users\Rainmaker\PycharmProjects\followinglinksinpython>python followinglinks.py
#Enter - http://py4e-data.dr-chuck.net/known_by_Bobby.html
#Enter count: 7
#Enter position: 18
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Bobby.html
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Temilade.html
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Reno.html
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Muriel.html
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Lilliarna.html
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Adana.html
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Avesta.html
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Azeem.html
#
#C:\Users\Rainmaker\PycharmProjects\followinglinksinpython>python followinglinks.py
#Enter - http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Enter count: 4
#Enter position: 3
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Montgomery.html
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Mhairade.html
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Butchi.html
#Retrieving:  http://py4e-data.dr-chuck.net/known_by_Anayah.html