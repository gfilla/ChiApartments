import requests
import sys
from bs4 import BeautifulSoup

search_params  = {'minAsk':500, 'maxAsk':1000, 'bedrooms':2}
base = 'http://chicago.craigslist.org/search/apa'
resp = requests.get(base, params=search_params)
resp.raise_for_status()  # <- no-op if status==200
Html_file= open('data/apartments.html','w+')
Html_file.write(resp.content)
Html_file.close()
print resp.content, resp.encoding
