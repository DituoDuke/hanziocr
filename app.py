from screenshot import capture_full_screen
from ocr import ocr
# from pinyin import get_definition
from pinyin import pinyinGenerateFromFile
from translate import translate
from cv import initiateFullImage
import sys
import os
import asyncio
from desktop_notifier import DesktopNotifier

import multiprocessing

notifier = DesktopNotifier(app_name="HanziOcr")

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
multiprocessing.freeze_support()


async def notificar(frase, traducao):
    encerrar = asyncio.Event()

    await notifier.send(
        title="Hanzi",
        message=f"text: {frase['text']}\nhanziPinyin: {''.join(frase['hanziPinyin'])}\nTradução: {traducao}",
        on_dismissed=lambda: encerrar.set(),
        on_clicked=lambda: encerrar.set()
    )

    # espera até dispensar ou 5 min
    await asyncio.wait_for(encerrar.wait(), timeout=30)
    sys.exit(0)

def main():
    capture_full_screen()
    initiateFullImage()
    ocr()
    frases = pinyinGenerateFromFile()
    with open(os.path.join(BASE_DIR, "results", "pinyin_results.txt"), 'w', encoding="utf-8") as file:
        file.write(f"text: {frases["text"]},\nhanziSegmented: {''.join(frases["hanziSegmented"])},\npinyin: {''.join([''.join(seg) for seg in frases["pinyin"]])},\nhanziPinyin: {''.join(frases["hanziPinyin"])}")
    traduzido = translate(frases["text"])
    with open(os.path.join(BASE_DIR, "results", "pinyin_results.txt"), 'a', encoding="utf-8") as file:
        file.write(f"\nTradução: {traduzido}")
    print(frases["hanziPinyin"])
    print(traduzido)
    asyncio.run(notificar(frases,traduzido))

if __name__ == '__main__':
    main()
