from joblib import load
import os
from .preprocess import normalize

MODEL_DIR = os.path.join(os.path.dirname(file), "model")
VEC_PATH = os.path.join(MODEL_DIR, "vectorizer.joblib")
CLS_PATH = os.path.join(MODEL_DIR, "classifier.joblib")



DEFAULT_INTENTS = {
"greet": "Hello! How can I help with registration today?",
"registration_dates": "Registration typically opens 2–3 weeks before classes. Check the portal for exact dates.",
"required_documents": "Common documents: ID proof, previous semester mark sheet, fee receipt, and course selection.",
"fee_payment": "Use the student portal payment section (UPI/net-banking/cards) and save the receipt.",
"portal_steps": "Login -> Registration -> Select courses -> Upload documents -> Pay fees -> Submit.",
"deadline": "Deadlines are posted on the portal; late submissions may incur a fee.",
"fallback": "I’m not sure yet. Try: registration dates, required documents, fee payment, or portal steps."
}

class IntentClassifier:
def init(self):
self.vectorizer = None
self.clf = None
if os.path.exists(VEC_PATH) and os.path.exists(CLS_PATH):
self.vectorizer = load(VEC_PATH)
self.clf = load(CLS_PATH)

text
def predict(self, text: str):
    if not self.vectorizer or not self.clf:
        t = normalize(text)
        if "date" in t or "when" in t or "deadline" in t:
            return "registration_dates", 0.61
        if "document" in t or "docs" in t or "upload" in t:
            return "required_documents", 0.62
        if "fee" in t or "payment" in t or "pay" in t:
            return "fee_payment", 0.64
        if "portal" in t or "register" in t or "steps" in t:
            return "portal_steps", 0.6
        if "hello" in t or "hi" in t:
            return "greet", 0.7
        return "fallback", 0.3
    X = self.vectorizer.transform([text])
    proba = getattr(self.clf, "predict_proba", None)
    if proba:
        conf = max(self.clf.predict_proba(X))
    else:
        conf = 0.75
    return self.clf.predict(X), float(conf)

def generate_reply(self, intent: str, entities: dict):
    return DEFAULT_INTENTS.get(intent, DEFAULT_INTENTS["fallback"])