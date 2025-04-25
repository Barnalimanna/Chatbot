from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample training
data = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "see you"],
    "thanks": ["thank you", "thanks a lot"]
}

X = []
y = []

for intent, phrases in data.items():
    X.extend(phrases)
    y.extend([intent] * len(phrases))

vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

clf = MultinomialNB()
clf.fit(X_vec, y)

def get_response(user_input):
    vec_input = vectorizer.transform([user_input])
    intent = clf.predict(vec_input)[0]
    return f"Intent detected: {intent}"
