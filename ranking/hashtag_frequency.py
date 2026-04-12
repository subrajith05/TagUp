from collections import Counter

def build_hashtag_frequency(df):
    all_tags = []

    for tags in df["hashtags"]:
        all_tags.extend([t.lower() for t in tags])

    freq = Counter(all_tags)

    return freq