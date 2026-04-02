from screenshot import capture_full_screen
from ocr import ocr
# from pinyin import get_definition
from pinyin import pinyinGenerateFromFile
from translate import translate
# top = int(input("cima: "))
# left = int(input("esquerda: " ))
# right = int(input("direita: " ))
# down = int(input("baixo: "))



# ocr()
frases = pinyinGenerateFromFile()
print(frases["hanziPinyin"])
print(translate(frases["text"]))
