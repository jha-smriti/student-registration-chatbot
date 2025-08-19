from flask import Blueprint, request, jsonify, current_app
from chatbot.schemas.chat import ChatRequestSchema
from chatbot.nlp.intent_classifier import IntentClassifier
from chatbot.nlp.entity_extractor import extract_entities
from chatbot.nlp.faq_retriever import FAQRetriever

chat_bp = Blueprint("chat", name)
classifier = IntentClassifier()
faq = FAQRetriever()

@chat_bp.route("/chat", methods=["POST"])
def chat():
data = request.get_json(force=True)
errors = ChatRequestSchema().validate(data)
if errors:
return jsonify({"error": errors}), 400
text = data["message"]
session_id = data["session_id"]

intent, confidence = classifier.predict(text)
entities = extract_entities(text)

answer = faq.lookup(text)
if answer:
    reply = answer
elif confidence >= current_app.config["CONF_THRESHOLD"]:
    reply = classifier.generate_reply(intent, entities)
else:
    reply = "I’m not fully sure. Did you mean: registration dates, required documents, fee payment, or portal steps?"

suggestions = ["registration dates", "required documents", "fee payment", "portal steps"]

return jsonify({
    "reply": reply,
    "intent": intent,
    "confidence": round(confidence, 3),
    "entities": entities,
    "suggestions": suggestions
}), 200
