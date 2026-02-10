from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

documents = [
    "I love machine learning",
    "Machine learning is fun",
    "I enjoy deep learning"
]

query = "machine learning"

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(documents + [query])

doc_vectors = tfidf[:-1]
query_vector = tfidf[-1]

scores = doc_vectors.dot(query_vector.T).toarray()

for i, score in enumerate(scores):
    print(f"Document {i+1} Score:", score[0])
