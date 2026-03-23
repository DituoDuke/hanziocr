from screenshot import capture_full_screen
from ocr import ocr
# from pinyin import get_definition
from pinyin import pinyinGenerateFromFile
# top = int(input("cima: "))
# left = int(input("esquerda: " ))
# right = int(input("direita: " ))
# down = int(input("baixo: "))


# capture_full_screen()
print(pinyinGenerateFromFile()["hanziPinyin"])