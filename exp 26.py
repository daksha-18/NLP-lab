from transformers import MarianMTModel, MarianTokenizer
model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

text = "Artificial Intelligence is changing the world."

inputs = tokenizer(text, return_tensors="pt", padding=True)
translated = model.generate(**inputs)

output = tokenizer.decode(translated[0], skip_special_tokens=True)

print("Original:", text)
print("Translated (French):", output)
