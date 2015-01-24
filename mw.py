from requests import session
import urllib, bs4
import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse, http.cookiejar
from urllib.parse import urlparse

username = 'mrzhangjiawei2008@gmail.com'
password = 'mrzhangjiawei2008'


cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

login_data = urllib.parse.urlencode({'login' : username, 'pass' : password}).encode('utf-8')

opener.open('https://secure.indeed.com/account/login', login_data)
resp = opener.open('http://www.indeed.com/jobs?q=developer&l=California')
html = resp.read()

xml = bs4.BeautifulSoup(html, "xml") #.find("REACH")['RANK']

print(xml)

