from flask import jsonify

from services.gmail_service import (
    fetch_unread_messages,
    get_email_content,
    get_gmail_service,
)
from tools.email_tool import apply_label, get_or_create_label
from tools.memory_tool import log_decision
from tools.semantic_tool import SemanticTool


class EmailPipeline:
    def __init__(self, service, agent):
        self.service = service
        self.agent = agent

    # def run(self):
    #     messages = fetch_unread_messages(self.service)

    #     print(f"Found {len(messages)} messages")

    #     for msg in messages:
    #         try:
    #             email = get_email_content(self.service, msg["id"])
    #             print("Processing:", email["subject"])

    #             decision = self.agent.process_email(email)
    #             print("Decision:", decision)

    #             # apply label
    #             if decision["action"] == "apply":
    #                 label_id = get_or_create_label(self.service, decision["label"])
    #                 apply_label(self.service, email["id"], label_id)

    #             # log memory (YOU IMPORTED IT BUT NEVER USED IT)
    #             log_decision(email, decision)

    #             # mark as read
    #             self.service.users().messages().modify(
    #                 userId="me",
    #                 id=email["id"],
    #                 body={"removeLabelIds": ["UNREAD"]},
    #             ).execute()

    #         except Exception as e:
    #             print("Error:", e)
    # ─────────────────────────────────────────────
    # CHANGE 1: pipeline.py
    # Make run() return results — only 3 additions
    # ─────────────────────────────────────────────

    def run(self):
        messages = fetch_unread_messages(self.service)
        print(f"Found {len(messages)} messages")

        results = []  # ← ADD

        for msg in messages:
            try:
                email = get_email_content(self.service, msg["id"])
                print("Processing:", email["subject"])

                decision = self.agent.process_email(email)
                print("Decision:", decision)

                if decision["action"] == "apply":
                    label_id = get_or_create_label(self.service, decision["label"])
                    apply_label(self.service, email["id"], label_id)

                log_decision(email, decision)

                self.service.users().messages().modify(
                    userId="me",
                    id=email["id"],
                    body={"removeLabelIds": ["UNREAD"]},
                ).execute()

                results.append(
                    {  # ← ADD
                        "id": email["id"],
                        "subject": email["subject"],
                        "body": email["body"][:300],
                        "action": decision["action"],
                        "label": decision["label"],
                        "confidence": round(decision["confidence"] * 100),
                    }
                )

            except Exception as e:
                print("Error:", e)
                results.append(
                    {  # ← ADD
                        "id": msg["id"],
                        "subject": "Error reading email",
                        "body": "",
                        "action": "error",
                        "label": None,
                        "confidence": 0,
                        "error": str(e),
                    }
                )

        return results  # ← ADD
