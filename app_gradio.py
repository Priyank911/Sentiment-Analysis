import gradio as gr
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

iface = gr.Interface(
    fn=analyze_sentiment, 
    inputs="text", 
    outputs="text",
    title="Sentiment Analysis",
    description="Enter text to analyze its sentiment."
)

if __name__ == "__main__":
    iface.launch()
