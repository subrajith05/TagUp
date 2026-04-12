import re

def normalize_text(text):
    # lowercase
    text = text.lower()

    # remove urls
    text = re.sub(r"http\S+|www\S+", "", text)

    # remove punctuation (keep words & numbers)
    text = re.sub(r"[^\w\s]", " ", text)

    # remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text