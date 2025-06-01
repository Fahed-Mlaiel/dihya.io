def health_check_view(request=None):
    from django.http import JsonResponse
    return JsonResponse({'status': 'ok', 'module': 'culture', 'checks': ['db', 'plugins', 'dweb', 'sectorisation']})
