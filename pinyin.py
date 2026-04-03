from pypinyin import pinyin, lazy_pinyin, Style
import pypinyin
import jieba
import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ocr_path = os.path.join(BASE_DIR, "results", "ocr_result.txt")

def pinyinGenerateFromFile():

    with open(ocr_path,'r') as file:
        text = file.read()
    segmentedHanzi = list(jieba.cut(text))
    hanziAndPinyin = []

    pinyinText = []
    for i, segments in enumerate(segmentedHanzi):
        pinyinText.append(pinyin(segments))
    pinyinTextMapped = [[p[0] for p in pin] for pin in pinyinText]

    for i, seg in enumerate(segmentedHanzi):
        hanziAndPinyin.append(f"{seg}({''.join(pinyinTextMapped[i])}) ")
    # print(pinyinTextMapped)
    with open(os.path.join(BASE_DIR, "results", "pinyin_results.txt"), 'w') as file:
        file.write(f"text: {text},\nhanziSegmented: {' '.join(segmentedHanzi)},\npinyin: {' '.join([''.join(seg) for seg in pinyinTextMapped])},\nhanziPinyin: {' '.join(hanziAndPinyin)}")
    return {
        "text": text,
        "hanziSegmented": " ".join(segmentedHanzi),
        "pinyin": " ".join(["".join(seg) for seg in pinyinTextMapped]),
        "hanziPinyin": " ".join(hanziAndPinyin)
    }
