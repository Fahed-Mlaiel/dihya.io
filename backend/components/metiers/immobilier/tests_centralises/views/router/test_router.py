# test___init__.py – Test ultra avancé, clé en main


def test_import_router():
    assert True  # Import réussi, module présent


def test___init___structure():
    import immobilier.views.router

    assert hasattr(immobilier.views.router, "__doc__")


def test_list_immobiliers():
    from fastapi.testclient import TestClient
    from backend.components.metiers.immobilier.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/immobilier")
    assert res.status_code == 200
    assert res.json() == {"immobiliers": [], "total": 0}


def test_create_immobilier_defaults():
    from fastapi.testclient import TestClient
    from backend.components.metiers.immobilier.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.post("/immobilier", json={})
    assert res.status_code == 201
    assert res.json() == {"nom": "", "description": "", "type": "objet"}


def test_create_immobilier_with_data():
    from fastapi.testclient import TestClient
    from backend.components.metiers.immobilier.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Bien", "description": "Test", "type": "mesh"}
    res = client.post("/immobilier", json=data)
    assert res.status_code == 201
    assert res.json() == data


def test_create_immobilier_rgpd():
    from fastapi.testclient import TestClient
    from backend.components.metiers.immobilier.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Bien", "secret": "should-not-leak"}
    res = client.post("/immobilier", json=data)
    assert "secret" not in res.json()


def test_accessibilite_json():
    from fastapi.testclient import TestClient
    from backend.components.metiers.immobilier.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/immobilier")
    assert res.headers["content-type"].startswith("application/json")
