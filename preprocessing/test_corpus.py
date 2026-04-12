from data.data_loader import load_dataset
from preprocessing.dataset_processor import build_corpus

df = load_dataset("data/tweets.csv")
df = build_corpus(df)

print(df.head())
print(df.iloc[0]["tokens"])
print(df.iloc[0]["hashtags"])
