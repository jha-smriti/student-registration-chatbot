import json
import os
from joblib import dump
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

DATA_DIR = os.path.join(os.path.dirname(file), "data")
INTENTS_PATH = os.path.join(DATA_DIR, "intents.json")
MODEL_DIR = os.path.join(os.path.dirname(file), "model")
def load_intents():
with open(INTENTS_PATH, "r", encoding="utf-8") as f:
data = json.load(f)
texts, labels = [], []
for intent, examples in data.items():
for ex in examples:
texts.append(ex)
labels.append(intent)
return texts, labels

def train():
X_texts, y = load_intents()
vec = TfidfVectorizer(ngram_range=(1,2), min_df=1, max_df=0.9)
X = vec.fit_transform(X_texts)
clf = LinearSVC()
clf.fit(X, y)

os.makedirs(MODEL_DIR, exist_ok=True)
dump(vec, os.path.join(MODEL_DIR, "vectorizer.joblib"))
dump(clf, os.path.join(MODEL_DIR, "classifier.joblib"))
print("Model trained and saved.")
if name == "main":
train()