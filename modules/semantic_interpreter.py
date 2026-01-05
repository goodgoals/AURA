import spacy

nlp = spacy.load("en_core_web_sm")

# Basic ontology for semantic mapping
ONTOLOGY = {
    "sleep": ["sleep", "rest", "nap", "recovery"],
    "run": ["run", "jog", "sprint", "exercise"],
    "fatigue": ["tired", "fatigue", "exhaustion", "weariness"],
    "fire": ["fire", "flame", "burning", "hot"],
    "ice": ["ice", "slippery", "frozen"],
    "code": ["code", "program", "python", "script"],
}

def embedding_score(word, concept):
    # simple synonym match for demo
    return 1.0 if word in ONTOLOGY.get(concept, []) else 0.0

class SemanticInterpreter:
    def __init__(self, ontology=ONTOLOGY):
        self.ontology = ontology

    def parse(self, query):
        doc = nlp(query.lower())
        tokens = [token.text for token in doc]
        concepts = []
        actions = []
        dependencies = []

        # Detect concepts
        for token in doc:
            for concept, synonyms in self.ontology.items():
                if embedding_score(token.text, concept) > 0.5 and concept not in concepts:
                    concepts.append(concept)

        # Detect actions (verbs)
        for token in doc:
            if token.pos_ in ["VERB", "AUX"]:
                actions.append(token.lemma_)

        # Extract basic dependency info
        for token in doc:
            if token.dep_ in ["nsubj", "dobj", "pobj"]:
                dependencies.append({"token": token.text, "dep": token.dep_, "head": token.head.text})

        return {
            "query": query,
            "tokens": tokens,
            "concepts": concepts,
            "actions": actions,
            "dependencies": dependencies
        }
