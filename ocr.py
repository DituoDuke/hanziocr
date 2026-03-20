import easyocr

ocr_path = "./results/ocr_result.txt"
capture_path = "./results/screenshot.png"

def ocr():
    reader = easyocr.Reader(['ch_sim', 'en'])
    resultArray = reader.readtext(capture_path, detail=0)
    resultString = ' '.join(resultArray)
    with open(ocr_path, 'w') as file:
        file.write(resultString)
    return resultString
