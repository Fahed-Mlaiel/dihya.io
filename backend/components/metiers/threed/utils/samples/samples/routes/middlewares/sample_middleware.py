# Middleware Python – Ultra avancé
def log_middleware(get_response):
    def middleware(request):
        print('Request:', getattr(request, 'method', None), getattr(request, 'path', None))
        return get_response(request)
    return middleware
