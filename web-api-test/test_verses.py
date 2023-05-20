import pytest
import requests

ENDPIONT  = 'https://api.quran.com/api/v4/'


def test_end_point():
    response = requests.get(ENDPIONT)
    assert response.status_code == 200

@pytest.mark.parametrize("chapter,verse", [('0', ''), ('1', '1:1'), ('2', '2:1'),
                                            ('113', '113:1'), ('114', '114:1'), ('115', ''), ])
def test_get_verses_by_chapter(chapter, verse):
    response_chapter = requests.get(ENDPIONT + f'verses/by_chapter/{chapter}')
    if chapter == '0' or chapter == '115':
        assert response_chapter.status_code == 404
    else:
        assert response_chapter.json()['verses'][0]['verse_key'] == verse

def test_get_verses_by_page():
    response_page = requests.get(ENDPIONT + 'verses/by_page/1')
    assert response_page.status_code == 200
    assert response_page.json()['verses'][0]['verse_key'] == '1:1'

@pytest.mark.parametrize("juz, verse", [('0', ''), ('1', '1:1'), ('2', '2:142'),
                                            ('29', '67:1'), ('30', '78:1'), ('31', ''), ])
def test_get_verses_by_juz(juz, verse):
    response_juz = requests.get(ENDPIONT + f'verses/by_juz/{juz}')
    if juz == '0' or juz == '31':
        assert response_juz.status_code == 404
    else:
        assert response_juz.json()['verses'][0]['verse_key'] == verse    