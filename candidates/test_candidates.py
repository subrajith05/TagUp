from features.keyword_extractor import extract_keywords
from candidates.generator import generate_hashtags
from features.tfidf_vectorizer import build_tfidf
from preprocessing.dataset_processor import build_corpus
from preprocessing.preprocess import preprocess
from data.data_loader import load_dataset

df = load_dataset("data/tweets.csv")
df = build_corpus(df)

vectorizer,_ = build_tfidf(df)

text = "Messi dominates Champions League match"

tokens = preprocess(text)
keywords = extract_keywords(text, vectorizer)

hashtags = generate_hashtags(tokens, keywords)

print("keywords:", keywords)
print("hashtags:", hashtags)