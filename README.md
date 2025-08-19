# student-registration-chatbot
Student Registration Chatbot: Flask + React assistant that automates registration FAQs and workflows with intent classification, FAQ search, and an embeddable web widget. Dockerized, deploy-ready.
Student Registration Chatbot
A lightweight, production-ready chatbot to automate student registration FAQs and workflows. Uses a classic NLP pipeline (TF-IDF + LinearSVC) for intents, rule/regex for entities, with REST endpoints and an embeddable React widget.

Features

20–30 intents for registration: dates, required documents, fee payment, portal steps, deadlines.

Confidence-based responses with clarifying questions and human handoff fallback.

FAQ retrieval for exact answers; admin routes to update FAQ.

REST hooks to Student Management System (stubbed, easy to integrate).

MongoDB for conversations and FAQ storage; Redis caching for performance.

React TypeScript chat widget: quick embed in any portal page.

Target ≥85% intent accuracy with curated training data.

Architecture

React widget -> Flask API (chat endpoint)

NLP pipeline: preprocess -> vectorize -> classify -> threshold -> enrich with entities -> select response

MongoDB for logs + FAQ; Redis for caching hot FAQs

Optional WebSocket for streaming responses

Quick Start

Clone
git clone https://github.com/your-username/student-registration-chatbot.git
cd student-registration-chatbot

Environment
cp .env.example .env

Fill values
Docker (recommended)
docker-compose up --build

Backend: http://localhost:8000
Frontend: http://localhost:5173

Dev (manual)
Backend
cd backend
python -m venv .venv && source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py

Frontend
cd frontend
npm install
npm run dev

Configuration (.env)

Backend
FLASK_ENV=development
SECRET_KEY=dev-secret
MONGO_URI=mongodb://mongo:27017/chatbot
REDIS_URL=redis://redis:6379/0
ALLOWED_ORIGINS=http://localhost:5173
CONF_THRESHOLD=0.6
ADMIN_TOKEN=change-me

SMS Integration
SMS_BASE_URL=https://sms.example.edu/api
SMS_API_KEY=replace_me

API Endpoints

POST /api/chat
Body: { session_id: string, message: string }
Resp: { reply, intent, confidence, entities, suggestions? }

GET /api/faqs
Resp: [{ question, answer, tags }]

POST /api/admin/faqs (requires header Authorization: Bearer ADMIN_TOKEN)
Body: { question, answer, tags? }

GET /health
Resp: { status: "ok" }

Training & Evaluation

Data: backend/chatbot/nlp/data/intents.json, faq.json

Train:
cd backend && python -m chatbot.nlp.train

Evaluate:
python -m chatbot.utils.evaluation

Folder Conventions

nlp/: preprocessing, classifier, entity extraction, training

routes/: Flask blueprints per domain

services/: Mongo/Redis/SMS clients, logging

schemas/: Pydantic-like validation via Marshmallow or dataclasses

Production Notes

Run with Gunicorn behind Nginx; enable CORS per domain.

Persist MongoDB volume; set robust SECRET_KEY and ADMIN_TOKEN.

Add rate limiting and request IDs for observability.

License
MIT



