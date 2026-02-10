from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

sentence = "I went to the bank to deposit money"
word = "bank"

sense = lesk(word_tokenize(sentence), word)
print("Best Sense:", sense)
print("Meaning:", sense.definition())
