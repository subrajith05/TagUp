from data.data_loader import load_dataset

from preprocessing.dataset_processor import build_corpus
from preprocessing.preprocess import preprocess

from features.tfidf_vectorizer import build_tfidf
from features.keyword_extractor import extract_keywords
from features.yake_extractor import extract_yake_keywords

from candidates.generator import generate_hashtags

from ranking.hashtag_frequency import build_hashtag_frequency
from ranking.ranker import rank_hashtags
from ranking.post_filter import post_filter
from ranking.cooccurrence import build_word_hashtag_map
from ranking.cooccurrence import infer_from_cooccurrence




class HashtagRecommender:
    def __init__(self, dataset_path):
        # load dataset
        df = load_dataset(dataset_path)

        # preprocessing
        df = build_corpus(df)

        # store dataset
        self.df = df

        # build TFIDF
        self.vectorizer, _ = build_tfidf(df)

        # build hashtag frequency
        self.freq = build_hashtag_frequency(df)

        #cooccurrence map
        self.word_tag_map = build_word_hashtag_map(df)

    def recommend(self, text, top_k=5):

        tokens = preprocess(text)

        tfidf_keywords = extract_keywords(text, self.vectorizer)
        yake_keywords = extract_yake_keywords(text)

        # keep keywords clean
        keywords = list(set(
            tfidf_keywords +
            yake_keywords
        ))

        candidates = generate_hashtags(tokens, keywords)

        ranked = rank_hashtags(
            candidates,
            " ".join(tokens),
            self.vectorizer,
            self.freq
        )

        co_tags = infer_from_cooccurrence(tokens, self.word_tag_map, top_k=2)

        ranked = rank_hashtags(
            candidates,
            " ".join(tokens),
            self.vectorizer,
            self.freq
        )

        # remove duplicates
        ranked = [tag for tag in ranked if tag not in co_tags]

        # co-occurrence first
        ranked = co_tags + ranked

        final = post_filter(ranked, top_k)

        return final


if __name__ == "__main__":
    model = HashtagRecommender("data/tweets.csv")

    text = "MMessi delivers another masterclass as Barcelona dominates the Champions League match."

    hashtags = model.recommend(text)

    print("Input:", text)
    print("Hashtags:", hashtags)