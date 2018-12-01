from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

data = load_files('../dataset/txt_sentoken', encoding="utf-8", decode_error="replace")
x_train, x_test, y_train, y_test = train_test_split(data.data, data.target)

# Use a TFIDF model with a vocabulary of the top 1000 most frequent words
vectorizer = TfidfVectorizer(stop_words="english", max_features=1000, decode_error="ignore")
tfidf_matrix = vectorizer.fit_transform(x_train)
