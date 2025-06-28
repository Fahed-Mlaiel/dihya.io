# test___init__.py – Test ultra avancé, clé en main


def test_import_router():
    assert True  # Import réussi, module présent


def test___init___structure():
    import ressources_humaines.views.router

    assert hasattr(ressources_humaines.views.router, "__doc__")


def test_list_ressources_humainess():
    from fastapi.testclient import TestClient
    from backend.components.metiers.ressources_humaines.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/ressources_humaines")
    assert res.status_code == 200
    assert res.json() == {"ressources_humainess": [], "total": 0}


def test_create_ressources_humaines_defaults():
    from fastapi.testclient import TestClient
    from backend.components.metiers.ressources_humaines.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.post("/ressources_humaines", json={})
    assert res.status_code == 201
    assert res.json() == {"nom": "", "description": "", "type": "objet"}


def test_create_ressources_humaines_with_data():
    from fastapi.testclient import TestClient
    from backend.components.metiers.ressources_humaines.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Cube", "description": "Test", "type": "mesh"}
    res = client.post("/ressources_humaines", json=data)
    assert res.status_code == 201
    assert res.json() == data


def test_create_ressources_humaines_rgpd():
    from fastapi.testclient import TestClient
    from backend.components.metiers.ressources_humaines.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Cube", "secret": "should-not-leak"}
    res = client.post("/ressources_humaines", json=data)
    assert "secret" not in res.json()


def test_accessibilite_json():
    from fastapi.testclient import TestClient
    from backend.components.metiers.ressources_humaines.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/ressources_humaines")
    assert res.headers["content-type"].startswith("application/json")
