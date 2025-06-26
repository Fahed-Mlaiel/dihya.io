"""
Middleware de traçabilité pour le module threed.
"""


def trace_context(request):
    trace_id = getattr(request, "trace_id", None)
    request.context = getattr(request, "context", {})
    request.context["trace_id"] = trace_id
    return request
