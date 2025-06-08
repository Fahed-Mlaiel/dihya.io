# Middleware imbriqué Python – Ultra avancé
def log_nested_middleware(get_response):
    def middleware(request):
        print('Nested Middleware:', getattr(request, 'method', None), getattr(request, 'path', None))
        return get_response(request)
    return middleware
