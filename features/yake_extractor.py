import yake

def extract_yake_keywords(text, top_k=5):
    kw_extractor = yake.KeywordExtractor(
        lan="en",
        n=2,
        dedupLim=0.9,
        top=top_k
    )

    keywords = kw_extractor.extract_keywords(text)

    cleaned = []
    for kw, score in keywords:
        words = kw.lower().split()
        cleaned.extend(words)

    return cleaned