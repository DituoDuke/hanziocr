from transformers import MarianMTModel, MarianTokenizer
import os
from pathlib import Path


def translate(texto):
    model_path = "./models/zh-en"

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

    # print(translated_texts[0])
    return translated_texts[0]

def translateChooseModel(texto, lang):
    model_path = "./models/"+lang

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