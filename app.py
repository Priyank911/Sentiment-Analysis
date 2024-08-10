from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        if 'text' not in data:
            return jsonify({'error': 'Missing "text" key in JSON data'}), 400
        
        text = data['text']
        analysis = TextBlob(text)
        sentiment = analysis.sentiment.polarity
        
        if sentiment > 0:
            result = "Positive"
        elif sentiment < 0:
            result = "Negative"
        else:
            result = "Neutral"
        
        return jsonify({'sentiment': result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
