from transformers import MarianMTModel, MarianTokenizer
import os
from pathlib import Path
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
capture_path = os.path.join(BASE_DIR, "results", "screenshot.png")

def translate(texto):
    model_path = os.path.join(BASE_DIR, "models", "zh-en")

    if not Path(model_path).exists():        
        model_name = 'Helsinki-NLP/opus-mt-zh-en'
        MarianTokenizer.from_pretrained(model_name).save_pretrained(model_path)
        MarianMTModel.from_pretrained(model_name).save_pretrained(model_path)
        print("modelo instalado")


    tokenizer = MarianTokenizer.from_pretrained(model_path)
    model = MarianMTModel.from_pretrained(model_path)


    inputs = tokenizer(texto, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)

    translated_texts = tokenizer.batch_decode(translated, skip_special_tokens=True)
    # with open(os.path.join(BASE_DIR, "results", "pinyin_results.txt"), 'a', encoding="utf-8") as file:
    #     file.write(f"\nTradução: {translated_texts[0]}")


    # print(translated_texts[0])
    return translated_texts[0]

def translateChooseModel(texto, lang):
    model_path = os.path.join(BASE_DIR, "models", lang)

    if not Path(model_path).exists():        
        model_name = 'Helsinki-NLP/opus-mt-'+lang
        MarianTokenizer.from_pretrained(model_name).save_pretrained(model_path)
        MarianMTModel.from_pretrained(model_name).save_pretrained(model_path)
        print("modelo instalado")


    tokenizer = MarianTokenizer.from_pretrained(model_path)
    model = MarianMTModel.from_pretrained(model_path)


    inputs = tokenizer(texto, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)

    translated_texts = tokenizer.batch_decode(translated, skip_special_tokens=True)

    # print(translated_texts[0])
    return translated_texts[0]
#translateChooseModel(input("Digite a frase: "), input("Escolha de qual lingua pra qual: "))
