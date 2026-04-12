from data.data_loader import load_dataset
from preprocessing.dataset_processor import build_corpus
from features.tfidf_vectorizer import build_tfidf
from features.keyword_extractor import extract_keywords

df = load_dataset("data/tweets.csv")
df = build_corpus(df)

vectorizer, _ = build_tfidf(df)

text = "Messi dominates Champions League match again"

keywords = extract_keywords(text, vectorizer)

print(keywords)