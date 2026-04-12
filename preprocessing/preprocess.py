from .expand_contractions import expand_contractions
from .normalize_text import normalize_text
from .tokenize_and_clean import tokenize_and_clean

def preprocess(text):
    text = expand_contractions(text)
    text = normalize_text(text)
    tokens = tokenize_and_clean(text)

    return tokens