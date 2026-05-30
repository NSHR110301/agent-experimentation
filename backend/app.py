import json

import requests
from agent.agent import EmailAgent
from flask import Flask, jsonify, request
from flask_cors import CORS
from services.gmail_service import get_gmail_service
from tools.semantic_tool import SemanticTool
from pipeline import EmailPipeline

app = Flask(__name__)
CORS(app)

# 🔹 Load rules once
with open("data/rules.json", "r") as f:
    rules = json.load(f)

# 🔹 Initialize system once (IMPORTANT)
semantic_tool = SemanticTool(rules)
agent = EmailAgent(semantic_tool)


# OPTIONAL (for real labeling later)
service = get_gmail_service()

email_pipeline = EmailPipeline(service, agent)


@app.route("/emails", methods=["GET"])
def process_inbox():
    try:
        results = email_pipeline.run()
        return jsonify({"emails": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/rules", methods=["POST"])
def update_rules():
    try:
        rules = request.json
        semantic_tool.update_rules(rules)
        # optionally save back to rules.json
        with open("data/rules.json", "w") as f:
            json.dump(rules, f, indent=2)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/process", methods=["POST"])
def process_email():
    try:
        data = request.json

        subject = data.get("subject", "")
        email_id = data.get("id", None)
        body = data.get("body", "")  # 👈 prevents crash

        email = {"subject": subject, "id": email_id, "body": body}

        decision = agent.process_email(email)

        # 🔥 OPTIONAL: apply label (can disable for now)
        if decision["action"] == "apply" and email_id:
            from tools.email_tool import apply_label, get_or_create_label

            label_id = get_or_create_label(service, decision["label"])
            apply_label(service, email_id, label_id)

        return jsonify(decision)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(port=5000, debug=True)
    print("🚀 Backend running at http://localhost:5000")
