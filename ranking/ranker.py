import numpy as np

def rank_hashtags(candidates, text, vectorizer, freq):
    tokens = text.split()

    scores = {}

    for tag in candidates:
        tag_words = split_hashtag(tag)

        # relevance score
        relevance = sum([
            word_score(word, vectorizer)
            for word in tag_words
        ])

        # frequency score
        f = freq.get(tag.lower(), 1)

        score = relevance + 0.1 * f

        scores[tag] = score

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return [tag for tag,_ in ranked]


def split_hashtag(tag):
    # split CamelCase
    words = []
    current = ""

    for c in tag:
        if c.isupper() and current:
            words.append(current.lower())
            current = c
        else:
            current += c

    words.append(current.lower())
    return words


def word_score(word, vectorizer):
    vocab = vectorizer.vocabulary_
    return 1 if word in vocab else 0