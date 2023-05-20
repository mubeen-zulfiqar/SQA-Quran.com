import requests

ENDPIONT  = 'https://api.quran.com/api/v4/'


def test_end_point():
    response = requests.get(ENDPIONT)
    assert response.status_code == 200

def test_juzs_present():
    response = requests.get(ENDPIONT + 'juzs')
    assert response.status_code == 200