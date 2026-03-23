from pypinyin import pinyin, lazy_pinyin, Style
import pypinyin
import jieba


def pinyinGenerateFromFile():
    ocr_path = "./results/ocr_result.txt"

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
    return {
        "text": text,
        "hanziSegmented": " ".join(segmentedHanzi),
        "pinyin": " ".join(["".join(seg) for seg in pinyinTextMapped]),
        "hanziPinyin": " ".join(hanziAndPinyin)
    }
