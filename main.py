from modules.semantic_interpreter import SemanticInterpreter
from modules.world_model import WorldModel
from modules.reasoning_engine import ReasoningEngine
from modules.api_layer import APILayer

# Initialize modules
semantic = SemanticInterpreter()
world = WorldModel()
reasoning = ReasoningEngine(world)
api = APILayer()

# Populate world model
world.add_relation("sleep", "reduces", "fatigue", confidence=1.0)
world.add_relation("rest", "reduces", "fatigue", confidence=0.9)
world.add_relation("fire", "is", "dangerous", confidence=1.0)
world.add_relation("ice", "is", "slippery", confidence=1.0)
world.add_relation("code", "enables", "programming", confidence=1.0)

# Context memory
context_memory = []

# Sample queries
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
    parsed = semantic.parse(q)
    result = reasoning.forward_chain(parsed["concepts"])
    context_memory.append(q)
    response_json = api.format_response(result, context_memory)
    print(f"Query: {q}\nAnswer: {response_json}\n{'-'*70}")
