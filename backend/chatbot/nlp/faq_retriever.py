import json
import os
from .preprocess import normalize

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "faq.json")

class FAQRetriever:
def init(self):
with open(DATA_PATH, "r", encoding="utf-8") as f:
self.faqs = json.load(f)

def lookup(self, query: str):
    qn = normalize(query)
    for item in self.faqs:
        if qn in item["question"].lower():
            return item["answer"]
    return None

def add(self, question: str, answer: str, tags=None):
    self.faqs.append({"question": question, "answer": answer, "tags": tags or []})

def list(self):
    return self.faqs
