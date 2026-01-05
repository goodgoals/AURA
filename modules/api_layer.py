import json

class APILayer:
    """
    Converts reasoning engine output into API-ready JSON
    """

    def format_response(self, reasoning_result, context_memory):
        response = {
            "answer": reasoning_result.get("answer", "Unknown"),
            "confidence": reasoning_result.get("confidence", 0.0),
            "reasoning_chain": reasoning_result.get("reasoning_chain", []),
            "assumptions": reasoning_result.get("assumptions", []),
            "conflicts": reasoning_result.get("conflicts", []),
            "context_memory": context_memory
        }
        return json.dumps(response, indent=2)
