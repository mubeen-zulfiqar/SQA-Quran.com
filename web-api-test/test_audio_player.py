import requests

ENDPIONT  = 'https://api.quran.com/api/v4/'


def test_end_point():
    response = requests.get(ENDPIONT)
    assert response.status_code == 200

def test_audio_by_chapter():
    response = requests.get(ENDPIONT + 'chapter_recitations/1/23')
    assert response.status_code == 200
    assert response.json()['audio_file']['chapter_id'] == 23
    assert response.json()['audio_file']['audio_url'] == 'https://download.quranicaudio.com/qdc/abdul_baset/mujawwad/23.mp3'

def test_audio_by_verse():
    response = requests.get(ENDPIONT + 'recitations/1/by_ayah/89:27')
    assert response.status_code == 200
    assert response.json()['audio_files'][0]['verse_key'] == '89:27'
    assert response.json()['audio_files'][0]['url'] == 'AbdulBaset/Mujawwad/mp3/089027.mp3'    