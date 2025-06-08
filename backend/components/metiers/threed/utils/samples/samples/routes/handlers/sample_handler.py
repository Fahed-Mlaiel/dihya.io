# Handler Python – Ultra avancé
def get_handler():
    def handler(request):
        return {"message": "Handler OK", "user": getattr(request, 'user', None)}
    return handler
