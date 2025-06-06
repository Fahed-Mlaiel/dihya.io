# sample_ai_helper.py – Exemple de helper IA (Python)
def sample_ai_helper(input):
    if not input:
        return {"status": "ERROR", "reason": "no input"}
    return {"status": "SAMPLE", "data": input, "audit": True}
