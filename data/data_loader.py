import pandas as pd

def load_dataset(path):
    df = pd.read_csv(path)

    # split hashtags column into list
    df["hashtags"] = df["hashtags"].apply(
        lambda x: [tag.strip() for tag in x.split(",")]
    )

    return df