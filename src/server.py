from flask import Flask, render_template, request, jsonify
from predict import pos_neg
from twitter import get_tweets
import json

with open('./mock-tweets.json') as fd:
    tweets = json.load(fd)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pos-neg', methods=['POST'])
def predict():
    body = request.get_json()
    topic = body['topic']
    # tweets = [{**tweet, 'prediction': pos_neg(tweet['text'])} for tweet in get_tweets(topic)]

    return jsonify({
        'tweets': tweets
    })
