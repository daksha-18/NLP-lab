import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | 'I' [0.4]
VP -> V NP [1.0]
Det -> 'a' [1.0]
N -> 'flight' [1.0]
V -> 'prefer' [1.0]
""")

parser = ViterbiParser(grammar)
sentence = "I prefer a flight".split()

for tree in parser.parse(sentence):
    print(tree)
