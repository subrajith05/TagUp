from main import HashtagRecommender
from data.data_loader import load_dataset
from preprocessing.dataset_processor import build_corpus
from evaluation.metrics import evaluate_dataset

model = HashtagRecommender("data/tweets.csv")

df = load_dataset("data/tweets.csv")
df = build_corpus(df)

results = evaluate_dataset(model, df, 3)

print(results)