from core.semantic_matcher import SemanticMatcher


class SemanticTool:
    def __init__(self, rules):
        self.matcher = SemanticMatcher(rules)

    def classify(self, subject: str, body: str) -> dict:
        label, confidence = self.matcher.classify(subject, body)

        return {"label": label, "confidence": confidence}

    def update_rules(self, rules):
        """Rebuild embeddings when user updates examples"""
        self.matcher = SemanticMatcher(rules)
