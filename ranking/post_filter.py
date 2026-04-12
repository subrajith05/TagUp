def post_filter(hashtags, top_k=5):
    seen = set()
    final = []

    for tag in hashtags:
        tag_lower = tag.lower()

        if tag_lower not in seen:
            seen.add(tag_lower)
            final.append(tag)

        if len(final) == top_k:
            break

    return final