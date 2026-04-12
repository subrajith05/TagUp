import numpy as np
from preprocessing.preprocess import preprocess

def extract_keywords(text, vectorizer, top_k=5):
    tokens = preprocess(text)
    doc = " ".join(tokens)

    tfidf_vector = vectorizer.transform([doc])
    scores = tfidf_vector.toarray()[0]

    feature_names = vectorizer.get_feature_names_out()

    # sort descending
    indices = np.argsort(scores)[::-1]

    keywords = []
    for idx in indices:
        if scores[idx] > 0:
            keywords.append(feature_names[idx])

        if len(keywords) == top_k:
            break

    return keywords