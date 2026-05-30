class EmailAgent:
    def __init__(self, semantic_tool):
        self.semantic_tool = semantic_tool

    def process_email(self, email: dict) -> dict:
        """
        email = {
            "id": str,
            "subject": str,
            "body": str
        }
        """

        result = self.semantic_tool.classify(email["subject"], email["body"])

        label = result["label"]
        confidence = result["confidence"]

        # --- Decision Logic (tune later) ---

        if confidence >= 0.65:
            return {"action": "apply", "label": label, "confidence": confidence}

        elif 0.4 <= confidence < 0.65:
            return {"action": "review", "label": label, "confidence": confidence}

        else:
            return {"action": "ignore", "label": None, "confidence": confidence}
