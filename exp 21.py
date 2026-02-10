import nltk
from nltk import pos_tag, word_tokenize, RegexpParser

sentence = "The intelligent student solved the problem"
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)

grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = RegexpParser(grammar)
tree = chunk_parser.parse(tags)

for subtree in tree.subtrees():
    if subtree.label() == "NP":
        print("Noun Phrase:", " ".join(word for word, tag in subtree))
