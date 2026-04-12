from preprocessing.preprocess import preprocess

def build_corpus(df):
    df["tokens"] = df["tweet"].apply(preprocess)
    return df