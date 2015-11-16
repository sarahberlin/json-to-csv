import requests
import bs4
import urllib

root_url = 'http://results.elections.virginia.gov/vaelections/2015%20November%20General/Site/Locality'
index_url = root_url + '/Index.html'

tagList = []
response = requests.get(index_url)
soup = bs4.BeautifulSoup(response.text)
for x in soup.select('li.hasLocal a[href]'):
		tagList.append(x.get_text().encode('utf-8').replace(' ','%20'))

jsonList = []
for tag in tagList:
	jsonList.append('http://results.elections.virginia.gov/vaelections/2015%20November%20General/Json/Locality/{0}/Index.json'.format(tag))
	
for json in jsonList[3:]:
	jsonid = json.replace('http://results.elections.virginia.gov/vaelections/2015%20November%20General/Json/Locality/','').replace(
		'%20','_').replace('/Index','')
	testfile = urllib.URLopener()
	testfile.retrieve(json, jsonid)