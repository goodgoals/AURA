import spacy

# Load small English model (can upgrade for real deployment)
nlp = spacy.load("en_core_web_sm")

# Simple ontology
ONTOLOGY = {
    "sleep": ["sleep", "rest", "nap"],
    "run": ["run", "jog", "sprint"],
    "fatigue": ["tired", "exhaustion", "fatigue"],
    "fire": ["fire", "flame", "burning"],
    "ice": ["ice", "slippery", "frozen"],
    "code": ["code", "program", "script", "python"],
}

def embedding_score(word, concept):
    return 1.0 if word in ONTOLOGY.get(concept, []) else 0.0

class SemanticInterpreter:
    def __init__(self, ontology):
        self.ontology = ontology

    def parse(self, query):
        doc = nlp(query.lower())
        tokens = [token.text for token in doc]
        concepts = []
        actions = []
        dependencies = []

        # Concepts extraction
        for token in tokens:
            for concept, synonyms in self.ontology.items():
                if embedding_score(token.text, concept) > 0.5 and concept not in concepts:
                    concepts.append(concept)

        # Actions extraction (verbs)
        for token in doc:
            if token.pos_ in ["VERB", "AUX"]:
                actions.append(token.lemma_)

        # Dependencies extraction
        for token in doc:
            if token.dep_ in ["nsubj", "dobj", "pobj"]:
                dependencies.append({"token": token.text, "dep": token.dep_, "head": token.head.text})

        return {
            "actions": actions,
            "concepts": concepts,
            "dependencies": dependencies,
            "raw_tokens": tokens
        }
