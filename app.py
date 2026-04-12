import gradio as gr
from main import HashtagRecommender

# load model once
model = HashtagRecommender("data/tweets.csv")


def predict(text):
    tags = model.recommend(text)
    return "   ".join(["#" + t for t in tags])


with gr.Blocks(theme=gr.themes.Soft()) as app:

    gr.Markdown(
        """
        # 🏷️ Twitter Hashtag Recommender
        Enter a tweet and get relevant hashtags instantly
        """
    )

    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(
                lines=3,
                placeholder="Type your tweet here...",
                label="Tweet"
            )

            btn = gr.Button("Generate Hashtags", variant="primary")

        with gr.Column():
            output = gr.Textbox(label="Suggested Hashtags")

    btn.click(
        fn=predict,
        inputs=text_input,
        outputs=output
    )

app.launch()