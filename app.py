from screenshot import capture_full_screen
from ocr import ocr
# from pinyin import get_definition
from pinyin import pinyinGenerateFromFile
from translate import translate
from cv import initiateFullImage
# top = int(input("cima: "))
# left = int(input("esquerda: " ))
# right = int(input("direita: " ))
# down = int(input("baixo: "))

import multiprocessing
multiprocessing.freeze_support()

def main():
    capture_full_screen()
    initiateFullImage()
    ocr()
    frases = pinyinGenerateFromFile()
    print(frases["hanziPinyin"])
    print(translate(frases["text"]))

if __name__ == '__main__':
    main()