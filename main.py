from modules.semantic_interpreter import SemanticInterpreter, ONTOLOGY
from modules.world_model import WorldModel

def main():
    interpreter = SemanticInterpreter(ONTOLOGY)
    world = WorldModel()

    queries = [
        "Do I need sleep to run?",
        "Should I rest before running?",
        "Is fire dangerous?",
        "Should we touch fire?",
        "Is ice slippery?",
        "Can we code in Python?",
        "Is sleep useful?"
    ]

    for q in queries:
        print(f"\nQuery: {q}")
        parsed = interpreter.parse(q)
        print("Parsed:", parsed)

        # Feed into world model (currently just adding concepts)
        world.update_concepts(parsed)
        print("World Model Updated.")
        world.debug_print()

if __name__ == "__main__":
    main()

