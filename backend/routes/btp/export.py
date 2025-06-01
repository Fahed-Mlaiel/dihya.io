def dweb_export_view(request=None):
    from django.http import JsonResponse
    return JsonResponse({'status': 'ok', 'export': 'dweb', 'module': 'btp'})
