# Handler imbriqué Python – Ultra avancé
def get_nested_handler():
    def handler(request):
        return {"message": "Nested Handler OK", "nested": True}
    return handler
