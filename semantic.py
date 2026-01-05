# -------------------------------
# Module 1: Semantic Interpreter
# -------------------------------

import spacy
from collections import defaultdict
import numpy as np

# Load small English model (can upgrade to large for real deployment)
nlp = spacy.load("en_core_web_sm")

# Simple ontology for demonstration
ONTOLOGY = {
    "sleep": ["sleep", "rest", "nap"],
    "run": ["run", "jog", "sprint"],
    "fatigue": ["tired", "exhaustion", "fatigue"],
    "fire": ["fire", "flame", "burning"],
    "ice": ["ice", "slippery", "frozen"],
    "code": ["code", "program", "script", "python"],
}

# Neural-style embedding scorer placeholder
# In real system, would use small neural network to score concept relevance
def embedding_score(word, concept):
    # Simplistic: 1 if exact match or in synonyms, else 0
    return 1.0 if word in ONTOLOGY.get(concept, []) else 0.0

class SemanticInterpreter:
    def __init__(self, ontology):
        self.ontology = ontology

    def parse(self, query):
        """
        Parse the natural language query into a structured concept graph.
        Returns:
            {
                "actions": [],
                "concepts": [],
                "dependencies": [],
                "raw_tokens": []
            }
        """
        doc = nlp(query.lower())
        tokens = [token.text for token in doc]
        concepts = []
        actions = []
        dependencies = []

        # Identify concepts
        for token in tokens:
            for concept, synonyms in self.ontology.items():
                score = embedding_score(token.text, concept)
                if score > 0.5 and concept not in concepts:
                    concepts.append(concept)

        # Identify verbs as actions
        for token in doc:
            if token.pos_ in ["VERB", "AUX"]:
                actions.append(token.lemma_)

        # Identify dependencies (simple dependency parse)
        for token in doc:
            if token.dep_ in ["nsubj", "dobj", "pobj"]:
                dependencies.append({"token": token.text, "dep": token.dep_, "head": token.head.text})

        return {
            "actions": actions,
            "concepts": concepts,
            "dependencies": dependencies,
            "raw_tokens": tokens
        }

# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    interpreter = SemanticInterpreter(ONTOLOGY)

    queries = [
        "Do I need sleep to run?",
        "Should I rest before running?",
        "Is fire dangerous?",
        "Can we code in Python?"
    ]

    for q in queries:
        parsed = interpreter.parse(q)
        print(f"Query: {q}")
        print("Parsed:", parsed)
        print("-" * 50)
