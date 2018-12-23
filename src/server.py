from flask import Flask, render_template, request, jsonify
from predict import pos_neg

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pos-neg', methods=['POST'])
def predict():
    body = request.get_json()
    topic = body['topic']
    res = pos_neg(topic)
    return jsonify(res)
