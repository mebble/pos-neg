import pickle
import json
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Get the data and labels
data = load_files('../dataset/txt_sentoken', encoding="utf-8", decode_error="replace")
x_train, x_test, y_train, y_test = train_test_split(data.data, data.target)
labels = [label for label in data.target_names]

print('Computing...')

# Use a TFIDF vectorizer with a vocabulary of the top 3000 most frequent words
vectorizer = TfidfVectorizer(stop_words="english", max_features=3000, decode_error="ignore")
vectorizer.fit(x_train)
x_train_vec = vectorizer.transform(x_train)
x_test_vec = vectorizer.transform(x_test)

# Create and train the model
model = LogisticRegression(solver='liblinear')
model.fit(x_train_vec, y_train)

# Test the model
predictions = model.predict(x_test_vec)
accuracy = accuracy_score(y_test, predictions)
print("The model's accuracy is {0:.2f}%".format(100 * accuracy))

print('Saving the labels...')
with open('labels.json', 'w') as fd:
    json.dump(labels, fd)

print('Pickling the model and the vectorizer...')
with open('model.pickle', 'wb') as fd:
    pickle.dump(model, fd)
with open('vectorizer.pickle', 'wb') as fd:
    pickle.dump(vectorizer, fd)

print('Trained and saved the model and vectorizer.')
