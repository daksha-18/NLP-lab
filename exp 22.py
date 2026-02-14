import spacy
nlp = spacy.load("en_core_web_sm")

text = """John went to the market. He bought apples.
Mary saw him there. She waved at John."""

doc = nlp(text)

resolved_text = text
last_noun = None

for token in doc:
    if token.pos_ == "PROPN":
        last_noun = token.text
    if token.pos_ == "PRON" and last_noun is not None:
        resolved_text = resolved_text.replace(token.text, last_noun)

print("Original Text:\n", text)
print("\nResolved Text:\n", resolved_text)
