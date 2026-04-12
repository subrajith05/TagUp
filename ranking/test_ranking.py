from data.data_loader import load_dataset
from preprocessing.dataset_processor import build_corpus
from preprocessing.preprocess import preprocess
from features.tfidf_vectorizer import build_tfidf
from features.keyword_extractor import extract_keywords
from features.yake_extractor import extract_yake_keywords
from candidates.generator import generate_hashtags
from ranking.hashtag_frequency import build_hashtag_frequency
from ranking.ranker import rank_hashtags
from post_filter import post_filter

df = load_dataset("data/tweets.csv")
df = build_corpus(df)

freq = build_hashtag_frequency(df)

vectorizer,_ = build_tfidf(df)

text = "Messi dominates Champions League match"

tokens = preprocess(text)
tfidf_keywords = extract_keywords(text, vectorizer)

yake_keywords = extract_yake_keywords(text)

keywords = list(set(tfidf_keywords + yake_keywords))

candidates = generate_hashtags(tokens, keywords)

ranked = rank_hashtags(candidates, text, vectorizer, freq)

final = post_filter(ranked, top_k=5)

print(final)