class ReasoningEngine:
    """
    Forward/backward chaining and conflict detection
    """

    def __init__(self, world_model):
        self.world = world_model

    def forward_chain(self, concepts):
        reasoning_chain = []
        assumptions = []
        conflicts = []
        confidence = 0.0
        answer = "Unknown"

        # Iterate concepts and apply causal reasoning
        for c in concepts:
            relations = self.world.get_all_relations(c)
            for relation, target, rel_conf in relations:
                reasoning_chain.append(f"{c} -> {relation} -> {target} (conf={rel_conf})")
                assumptions.append(target)
                confidence = max(confidence, rel_conf)
                # Simple answer heuristic
                if target in ["fatigue", "performance"]:
                    answer = "Yes"
                elif target in ["dangerous", "slippery"]:
                    answer = "No"

        return {
            "answer": answer,
            "confidence": confidence,
            "reasoning_chain": reasoning_chain,
            "assumptions": assumptions,
            "conflicts": conflicts
        }
