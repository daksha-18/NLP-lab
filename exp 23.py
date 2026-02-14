import spacy
from itertools import combinations

nlp = spacy.load("en_core_web_md")

text = """Artificial Intelligence is transforming industries.
Machine learning is a subset of AI.
Bananas are yellow in color.
Deep learning is widely used today."""

doc = nlp(text)

sentences = list(doc.sents)

similarities = []
for s1, s2 in combinations(sentences, 2):
    sim = s1.similarity(s2)
    similarities.append(sim)

coherence_score = sum(similarities) / len(similarities)

print("Text:\n", text)
print("\nCoherence Score:", round(coherence_score, 3))

if coherence_score > 0.5:
    print("The text is coherent.")
else:
    print("The text is NOT coherent.")
