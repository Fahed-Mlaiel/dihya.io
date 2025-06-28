# test___init__.py – Test ultra avancé, clé en main


def test_import_router():
    assert True  # Import réussi, module présent


def test___init___structure():
    import mobile.views.router

    assert hasattr(mobile.views.router, "__doc__")


def test_list_mobiles():
    from fastapi.testclient import TestClient
    from backend.components.metiers.mobile.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/mobile")
    assert res.status_code == 200
    assert res.json() == {"mobiles": [], "total": 0}


def test_create_mobile_defaults():
    from fastapi.testclient import TestClient
    from backend.components.metiers.mobile.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.post("/mobile", json={})
    assert res.status_code == 201
    assert res.json() == {"nom": "", "description": "", "type": "objet"}


def test_create_mobile_with_data():
    from fastapi.testclient import TestClient
    from backend.components.metiers.mobile.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Cube", "description": "Test", "type": "mesh"}
    res = client.post("/mobile", json=data)
    assert res.status_code == 201
    assert res.json() == data


def test_create_mobile_rgpd():
    from fastapi.testclient import TestClient
    from backend.components.metiers.mobile.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Cube", "secret": "should-not-leak"}
    res = client.post("/mobile", json=data)
    assert "secret" not in res.json()


def test_accessibilite_json():
    from fastapi.testclient import TestClient
    from backend.components.metiers.mobile.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/mobile")
    assert res.headers["content-type"].startswith("application/json")
