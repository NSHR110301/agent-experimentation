from sentence_transformers import SentenceTransformer, util


class SemanticMatcher:

    def __init__(self, rules):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.label_embeddings = self._build_embeddings(rules)

    def _build_embeddings(self, rules):
        label_embeddings = {}

        for label, examples in rules.items():
            embeddings = self.model.encode(examples, convert_to_tensor=True)
            label_embeddings[label] = embeddings

        return label_embeddings

    def classify(self, subject, body):
        text = subject + " " + body

        email_embedding = self.model.encode(text, convert_to_tensor=True)

        best_label = None
        best_score = -1

        for label, embeddings in self.label_embeddings.items():

            scores = util.cos_sim(email_embedding, embeddings)
            max_score = scores.max().item()

            if max_score > best_score:
                best_score = max_score
                best_label = label

        return best_label, best_score
