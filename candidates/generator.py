from nltk import pos_tag

def camel_case(words):
    return "".join(w.capitalize() for w in words)


def generate_hashtags(tokens, keywords):
    hashtags = set()

    # single words
    for word in keywords:
        hashtags.add(word.lower())

    # POS tags
    pos = pos_tag(tokens)

    for i in range(len(pos) - 1):
        w1, t1 = pos[i]
        w2, t2 = pos[i + 1]

        # allow noun-noun only
        if (
            (t1.startswith("NNP") and t2.startswith("NNP")) or
            (t1.startswith("JJ") and t2.startswith("NN")) or
            (t1.startswith("NN") and t2.startswith("NN"))
        ):
            hashtags.add(camel_case([w1, w2]))

    return list(hashtags)