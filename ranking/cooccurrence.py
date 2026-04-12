from collections import defaultdict, Counter

def build_word_hashtag_map(df):
    mapping = defaultdict(Counter)

    for _, row in df.iterrows():
        tokens = row["tokens"]
        hashtags = [h.lower() for h in row["hashtags"]]

        for token in tokens:
            for tag in hashtags:
                mapping[token][tag] += 1

    return mapping


def infer_from_cooccurrence(tokens, mapping, top_k=3):
    tag_scores = Counter()
    tag_support = defaultdict(set)

    for token in tokens:
        if token in mapping:
            for tag, count in mapping[token].items():
                tag_scores[tag] += count
                tag_support[tag].add(token)

    # require >=2 tokens supporting tag
    filtered = {
        tag: score
        for tag, score in tag_scores.items()
        if len(tag_support[tag]) >= 2
    }

    ranked = sorted(filtered.items(), key=lambda x: x[1], reverse=True)

    return [tag for tag,_ in ranked[:top_k]]