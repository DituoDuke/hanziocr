from pypinyin import pinyin, lazy_pinyin, Style
import pypinyin
import jieba

ocr_path = "./results/ocr_result.txt"

with open(ocr_path,'r') as file:
    text = file.read()

segmentedHanzi = list(jieba.cut(text))

pinyinText = []
print(list(segmentedHanzi))
for segments in range(len(segmentedHanzi)):
    pinyinText.append(pinyin(segmentedHanzi[segments]))


print(pinyin(pinyinText[0]))
