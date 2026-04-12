def normalize(tags):
    return set(
        t.lower().replace("#", "").strip()
        for t in tags
    )


def hit_rate_at_k(true_tags, pred_tags, k=5):

    true = normalize(true_tags)
    pred = normalize(pred_tags[:k])

    return 1 if true & pred else 0


def precision_at_k(true_tags, pred_tags, k=5):

    true = normalize(true_tags)
    pred = normalize(pred_tags[:k])

    return len(true & pred) / k


def recall_at_k(true_tags, pred_tags, k=5):

    true = normalize(true_tags)
    pred = normalize(pred_tags[:k])

    return len(true & pred) / len(true)


def evaluate_dataset(model, df, k=5):

    hit_scores = []
    precision_scores = []
    recall_scores = []

    for _, row in df.iterrows():

        text = row["tweet"]
        true_tags = row["hashtags"]

        pred = model.recommend(text)

        hit_scores.append(hit_rate_at_k(true_tags, pred, k))
        precision_scores.append(precision_at_k(true_tags, pred, k))
        recall_scores.append(recall_at_k(true_tags, pred, k))

    hit = sum(hit_scores) / len(hit_scores)
    precision = sum(precision_scores) / len(precision_scores)
    recall = sum(recall_scores) / len(recall_scores)

    return {
        "Hit@{}".format(k): hit,
        "Precision@{}".format(k): precision,
        "Recall@{}".format(k): recall
    }