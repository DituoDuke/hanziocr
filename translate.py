from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-zh-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)


inputs = tokenizer("我爱我的家人", return_tensors="pt", padding=True, truncation=True)
translated = model.generate(**inputs)

translated_texts = tokenizer.batch_decode(translated, skip_special_tokens=True)

print(translated_texts[0])