def validate_project_payload(*args, **kwargs):
    return True

def role_required(*args, **kwargs):
    def decorator(f):
        return f
    return decorator

def log_audit_event(*args, **kwargs):
    pass
