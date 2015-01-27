from requests import session
import urllib, urllib2, cookielib, bs4
from urlparse import urlparse
import collections

username = 'mrzhangjiawei2008@gmail.com'
password = 'mrzhangjiawei2008'

domainname='http://www.indeed.com'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'login' : username, 'pass' : password})

opener.open('https://secure.indeed.com/account/login', login_data)

jobdict = dict()


counter=0
curind=0
indperpage=50
maxind=200

searchquery = 'http://www.indeed.com/jobs?q=developer&l=California&limit=50'

f=open("indeeddict.out","w")

#while curind<maxind:
    
qry = searchquery
if curind>0:
    qry=qry+'&start='+str(curind)
#curind+=indperpage

resp = opener.open(qry)
html = resp.read()

#    with open("indeed.out","w") as f:
#        f.write(str(html))

soup = bs4.BeautifulSoup(html)

for a in soup.findAll('a', class_='jobtitle'):
    #if a['class']=='jobtitle':
        temp= dict()
        temp['jobtitle']=a.text
        temp['link']=domainname+a['href']
        jobdict[counter]=temp
        counter+=1
for a in soup.findAll('a'):
    if '/rc/clk' in a['href']:
        temp= dict()
        temp['jobtitle']=a.text
        temp['link']=domainname+a['href']
        jobdict[counter]=temp
        counter+=1

f.write(str(jobdict))
f.close()












