from nltk.corpus import wordnet as wn

word = "bank"
synsets = wn.synsets(word)

for syn in synsets:
    print("Name:", syn.name())
    print("Meaning:", syn.definition())
    print("Examples:", syn.examples())
    print()
