import requests
import sys
from bs4 import BeautifulSoup


def fetch_search_results(query=None, minAsk=None, maxAsk=None, bedrooms=None):
    search_params = {
        key: val for key, val in locals().items() if val is not None
    }
    if not search_params:
        raise ValueError("No valid keywords")

    base = 'http://chicago.craigslist.org/search/apa'
    resp = requests.get(base, params=search_params, timeout=3)
    resp.raise_for_status()  # <- no-op if status==200
    Html_file= open('/data/apartments.html',"w")
    Html_file.write(resp.content)
    Html_file.close()
    return resp.content, resp.encoding


def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, from_encoding=encoding)
    return parsed

def extract_listings(parsed):
    listings = parsed.find_all('p', class_='row')
    return listings

def read_search_results(file_name):
    myf = open(file_name,'r')
    return myf.read() , 'utf-8'



if __name__ == '__main__':
    test_file = 'data/apartments.html'
    encoding = 'utf-8'
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        html, encoding = read_search_results(test_file)
    else:
        html, encoding = fetch_search_results(
            minAsk=500, maxAsk=1000, bedrooms=2
        )
    doc = parse_source(html, encoding)
    listings = extract_listings(doc) # add this line
    print len(listings)              # and this one
    print listings[0].prettify()     # and this one too
