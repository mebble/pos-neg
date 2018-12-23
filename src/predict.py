import pickle
import json

print('Loading the labels...')
with open('labels.json') as fd:
    labels = json.load(fd)

print('Loading the pickles...')
with open('model.pickle', 'rb') as fd:
    model = pickle.load(fd)
with open('vectorizer.pickle', 'rb') as fd:
    vectorizer = pickle.load(fd)
print('Done')

def pos_neg(topic):
    topic_vec = vectorizer.transform([topic])
    prediction = model.predict(topic_vec)[0]
    prediction_proba = model.predict_proba(topic_vec)[0]

    probs = {labels[i]: prob for i, prob in enumerate(prediction_proba.tolist())}

    result = {
        'label': labels[prediction],
        'probabilities': probs
    }

    return result
