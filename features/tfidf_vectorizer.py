from sklearn.feature_extraction.text import TfidfVectorizer

def build_tfidf(df):
    # tokens -> string
    documents = df["tokens"].apply(lambda x: " ".join(x))

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    return vectorizer, tfidf_matrix