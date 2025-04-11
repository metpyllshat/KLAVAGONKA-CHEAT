from config import API_KEY
import requests
import json
import keyboard

def ocr_space_file(filename, overlay=False, api_key=API_KEY, language='rus'):

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'scale': 'true',
               'OCREngine': 2,
               'detectOrientation': 'true'
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return json.loads(r.content.decode())["ParsedResults"][0]["ParsedText"]