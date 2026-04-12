from data.data_loader import load_dataset
from preprocessing.dataset_processor import build_corpus
from features.tfidf_vectorizer import build_tfidf

df = load_dataset("data/tweets.csv")
df = build_corpus(df)

vectorizer, tfidf_matrix = build_tfidf(df)

print(tfidf_matrix.shape)
print(len(vectorizer.get_feature_names_out()))