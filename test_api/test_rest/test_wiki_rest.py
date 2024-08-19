import requests
import pytest

S = requests.Session()

def get_sites(lat, long, radius, limit=100):
    URL = 'http://en.wikipedia.org/w/api.php'
    PARAMS = {
        'format': "json",
        'list': 'geosearch',
        'gscoord': f'{lat}|{long}',
        'gslimit': f'{limit}',
        'gsradius': f'{radius}',
        'action': 'query'
    }
    r = S.get(url=URL, params=PARAMS)
    pages = r.json()['query']['geosearch']
    sites = [page['title'] for page in pages]
    return sites

@pytest.mark.exc
def test_get_site(coord, text):
    assert text in get_sites(*coord, radius=100)

