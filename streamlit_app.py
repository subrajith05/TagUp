import streamlit as st
from main import HashtagRecommender

st.set_page_config(
    page_title="Twitter Hashtag Recommender",
    page_icon="🏷️",
    layout="centered"
)

@st.cache_resource
def load_model():
    return HashtagRecommender("data/tweets.csv")

model = load_model()

st.title("🏷️ TagUp - A Twitter Hashtag Recommender")
st.write("Enter a tweet to generate relevant hashtags")

text = st.text_area(
    "Tweet",
    placeholder="Enter your tweet..."
)

# USER SELECT K
k = st.slider(
    "Number of hashtags (K)",
    min_value=1,
    max_value=10,
    value=5
)

if st.button("Generate Hashtags"):

    if text.strip():

        tags = model.recommend(text, top_k=k)

        st.subheader("Suggested Hashtags")

        tag_html = ""
        for tag in tags:
            tag_html += f"""
            <span style="
                display:inline-block;
                padding:8px 14px;
                margin:6px;
                background:#1f2937;
                border-radius:10px;
                font-size:14px;
            ">#{tag}</span>
            """

        st.markdown(tag_html, unsafe_allow_html=True)

    else:
        st.warning("Enter a tweet first")