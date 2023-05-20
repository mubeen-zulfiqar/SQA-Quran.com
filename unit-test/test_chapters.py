import requests

ENDPIONT  = 'https://api.quran.com/api/v4/'


def test_end_point():
    response = requests.get(ENDPIONT)
    assert response.status_code == 200

def test_chapters_present():
    response = requests.get(ENDPIONT + 'chapters?language=en')
    assert response.status_code == 200

def test_get_chapter_by_id():
    response_chapter_0 = requests.get(ENDPIONT + 'chapters/0?language=en')
    assert response_chapter_0.status_code == 404

    response_chapter_1 = requests.get( ENDPIONT + 'chapters/1?language=en')
    assert  response_chapter_1.status_code == 200
    assert response_chapter_1.json()['chapter']['name_complex'] == "Al-Fātiĥah"

    response_chapter_2 = requests.get( ENDPIONT + 'chapters/2?language=en')
    assert  response_chapter_2.status_code == 200
    assert response_chapter_2.json()['chapter']['name_complex'] == "Al-Baqarah"

    response_chapter_113 = requests.get( ENDPIONT + 'chapters/113?language=en')
    assert  response_chapter_113.status_code == 200
    assert response_chapter_113.json()['chapter']['name_complex'] == "Al-Falaq"

    response_chapter_114 = requests.get( ENDPIONT + 'chapters/114?language=en')
    assert  response_chapter_114.status_code == 200
    assert response_chapter_114.json()['chapter']['name_complex'] == "An-Nās"

    response_chapter_115 = requests.get(ENDPIONT + 'chapters/115?language=en')
    assert response_chapter_115.status_code == 404


def test_get_chapter_info__by_id():
    response_chapter_0 = requests.get(ENDPIONT + 'chapters/0/info?language=en')
    assert response_chapter_0.status_code == 404

    response_chapter_1 = requests.get( ENDPIONT + 'chapters/1/info?language=en')
    assert  response_chapter_1.status_code == 200
    assert "Al-Fatihah" in response_chapter_1.json()['chapter_info']['short_text']

    response_chapter_2 = requests.get( ENDPIONT + 'chapters/2/info?language=en')
    assert  response_chapter_2.status_code == 200
    assert "Al-Baqarah" in response_chapter_2.json()['chapter_info']['short_text']

    response_chapter_113 = requests.get( ENDPIONT + 'chapters/113/info?language=en')
    assert  response_chapter_113.status_code == 200
    assert "Al Falaq" in response_chapter_113.json()['chapter_info']['text']

    response_chapter_114 = requests.get( ENDPIONT + 'chapters/114/info?language=en')
    assert  response_chapter_114.status_code == 200
    assert "An Nas" in response_chapter_114.json()['chapter_info']['text']

    response_chapter_115 = requests.get(ENDPIONT + 'chapters/115/info?language=en')
    assert response_chapter_115.status_code == 404
