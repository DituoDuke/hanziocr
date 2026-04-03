import easyocr
import os

import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ocr_path = os.path.join(BASE_DIR, "results", "ocr_result.txt")
capture_path = os.path.join(BASE_DIR, "results", "screenshot.png")

def ocr():
    reader = easyocr.Reader(['ch_sim', 'en'])
    resultArray = reader.readtext(capture_path, detail=0)
    resultString = ' '.join(resultArray)
    with open(ocr_path, 'w') as file:
        file.write(resultString)
    return resultString
