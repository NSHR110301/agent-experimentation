import json

import pipeline
from agent.agent import EmailAgent
from pipeline import EmailPipeline
from services.gmail_service import (
    fetch_unread_messages,
    get_email_content,
    get_gmail_service,
)
from tools.email_tool import apply_label, get_or_create_label
from tools.semantic_tool import SemanticTool

# 🔹 Step 1: Define rules
with open("data/rules.json", "r") as f:
    rules = json.load(f)


def main():
    print("Starting system...")

    service = get_gmail_service()
    semantic_tool = SemanticTool(rules)
    agent = EmailAgent(semantic_tool)

    pipeline = EmailPipeline(service, agent)
    pipeline.run()


if __name__ == "__main__":
    main()
