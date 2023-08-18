import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

nltk.download("punkt")

text = """
Machine learning is a branch of artificial intelligence that allows computers to learn and improve from experience without being explicitly programmed. It is the process of using algorithms and statistical models to analyze and draw insights from large amounts of data, and then use those insights to make predictions or decisions. Machine learning has become increasingly popular in recent years, as the amount of available data has grown and computing power has increased.
There are three main types of machine learning: supervised learning, unsupervised learning, and reinforcement learning. In supervised learning, the algorithm is given a labeled dataset and learns to make predictions based on that data. In unsupervised learning, the algorithm is given an unlabeled dataset and must find patterns and relationships within the data on its own. In reinforcement learning, the algorithm learns by trial and error, receiving feedback in the form of rewards or punishments for certain actions.
Machine learning is used in a wide range of applications, including image recognition, natural language processing, autonomous vehicles, fraud detection, and recommendation systems. As the technology continues to improve, it is likely that machine learning will become even more prevalent in our daily lives.
"""

sentences = nltk.sent_tokenize(text)

vectorizer = CountVectorizer(stop_words="english")
sentence_vectors = vectorizer.fit_transform(sentences)

similarity_matrix = cosine_similarity(sentence_vectors)

graph = nx.from_numpy_array(similarity_matrix)

scores = nx.pagerank_numpy(graph)

num_sentences = 3
top_sentence_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:num_sentences]

summary = [sentences[i] for i in top_sentence_indices]

print("Summary:\n")
print("\n".join(summary))