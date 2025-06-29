"""Logger structuré Python pour l’audit"""

def log_audit(event, level="INFO"):
    print(f"AUDIT | {level} | {event}")
