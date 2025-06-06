"""
db.py – Mock DB ultra avancé pour l’API Threed (Python)
Inclut : find_by_id, insert, update, delete
"""
def db_find_by_id(table, id):
    return {"id": id, "name": "Cube Ultra", "status": "active"}

def db_insert(table, data):
    return {**data, "id": 2}

def db_update(table, id, data):
    return {**data, "id": id}

def db_delete(table, id):
    return True
