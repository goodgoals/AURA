class WorldModel:
    """
    Causal knowledge graph with confidence scores
    """

    def __init__(self):
        self.graph = {}  # concept -> {"relations": [(relation, target, confidence)]}

    def add_concept(self, concept):
        if concept not in self.graph:
            self.graph[concept] = {"relations": []}

    def add_relation(self, source, relation, target, confidence=1.0):
        self.add_concept(source)
        self.add_concept(target)
        self.graph[source]["relations"].append((relation, target, confidence))

    def query_relation(self, source, target):
        if source not in self.graph:
            return []
        return [rel for rel in self.graph[source]["relations"] if rel[1] == target]

    def get_all_relations(self, concept):
        return self.graph.get(concept, {}).get("relations", [])

    def debug_print(self):
        print("=== World Model Graph ===")
        for concept, data in self.graph.items():
            print(f"{concept}: {data['relations']}")
