# TagUp — A Deterministic Twitter Hashtag Recommender

TagUp recommends hashtags for a tweet using classic NLP techniques — TF-IDF and YAKE keyword extraction, candidate generation, and frequency/co-occurrence-based ranking — with **no embeddings, no neural network, and no similarity search**. It ships with a Streamlit app for interactive use.

## How it works

The core is the `HashtagRecommender` class (`main.py`), built once per dataset:

1. **Load & preprocess** — loads the tweet dataset (`data/data_loader.py`) and builds a cleaned corpus (`preprocessing/dataset_processor.py`).
2. **Index building (on init)** — fits a TF-IDF vectorizer over the corpus, builds a hashtag frequency table, and builds a word → hashtag co-occurrence map.
3. **Recommend (per query tweet)**:
   - Normalizes casual/social-media text (`preprocessing/cecs.py`).
   - Tokenizes and preprocesses the tweet (`preprocessing/preprocess.py`).
   - Extracts keywords two ways — TF-IDF-weighted terms and **YAKE** keywords (`features/`) — and merges them.
   - Generates hashtag candidates from the tokens + keywords (`candidates/generator.py`).
   - Ranks candidates using TF-IDF similarity and historical hashtag frequency (`ranking/ranker.py`, `ranking/hashtag_frequency.py`).
   - Separately infers hashtags from the word/hashtag co-occurrence map (`ranking/cooccurrence.py`) and merges them in ahead of the ranked list.
   - Applies a final post-filter (`ranking/post_filter.py`) and returns the top-*k* hashtags.

## Repository structure

```
.
├── data/                    # Dataset + data loading (data_loader.py)
├── preprocessing/           # Corpus building, casual-text normalization, tokenization
├── features/                # TF-IDF vectorizer, keyword extraction, YAKE extraction
├── candidates/               # Hashtag candidate generation
├── ranking/                  # Frequency ranking, co-occurrence inference, post-filtering
├── evaluation/                # Evaluation metrics (evaluate_dataset)
├── main.py                    # HashtagRecommender class
├── evaluate.py                 # Script to run evaluation over a dataset
├── streamlit_app.py             # Interactive Streamlit UI
├── setup.py
├── requirements.txt
└── README.md
```

## Requirements

```bash
pip install -r requirements.txt
```

(`streamlit`, `pandas`, `scikit-learn`, `nltk`, `yake`, `numpy`)

## Usage

### Interactive app

```bash
streamlit run streamlit_app.py
```

Enter a tweet, pick how many hashtags (K) to generate, and get suggestions rendered as tags.

### Programmatic use

```python
from main import HashtagRecommender

model = HashtagRecommender("data/tweets.csv")
tags = model.recommend("just watched the match, what a comeback!", top_k=5)
print(tags)
```

### Evaluation

```bash
python evaluate.py
```

Loads the dataset, builds the corpus, and runs `evaluate_dataset` from `evaluation/metrics.py` against the model at a fixed *k*.

## Related: an embedding-based comparison

We also built **[HashTagRecommendation-Full-Tweet-Comparison](https://github.com/VarunUdayakumar/HashTagRecommendation-Full-Tweet-Comparison)**, which tackles the same problem with FastText and BERT tweet embeddings plus FAISS similarity search instead of TF-IDF/YAKE and co-occurrence ranking. It's a good side-by-side if you're curious how a learned-embedding approach stacks up against this deterministic one — spoiler: TagUp came out ahead in our tests.
