from data_loader import load_dataset

df = load_dataset("tweets.csv")

print(df.head())
print(df.iloc[0])

print(type(df["hashtags"][0]))
print(df["hashtags"][0])
print(len(df["hashtags"][0]))