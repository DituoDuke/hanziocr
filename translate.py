import os
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from transformers import MarianMTModel, MarianTokenizer

def translate(text, src, tgt):
    model_name = f"Helsinki-NLP/opus-mt-{src}-{tgt}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    tokens = tokenizer([text], return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# zh → en → pt
en = translate("很高兴认识你（我爱你）", "zh", "en")
pt = translate(en, "en", "pt")
print(pt)