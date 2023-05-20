import requests

ENDPIONT  = 'https://api.quran.com/api/v4/'


def test_end_point():
    response = requests.get(ENDPIONT)
    assert response.status_code == 200

def test_search_by_word():
    response = requests.get(ENDPIONT + 'search?q=O%20tranquil%20soul%21&language=en')
    assert response.status_code == 200
    assert response.json()['search']['results'][0]['verse_key'] == '89:27'