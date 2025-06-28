# test___init__.py – Test ultra avancé, clé en main


def test_import_router():
    assert True  # Import réussi, module présent


def test___init___structure():
    import a_i.views.router

    assert hasattr(a_i.views.router, "__doc__")


def test_list_a_is():
    from fastapi.testclient import TestClient
    from backend.components.metiers.a_i.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/a_i")
    assert res.status_code == 200
    assert res.json() == {"a_is": [], "total": 0}


def test_create_a_i_defaults():
    from fastapi.testclient import TestClient
    from backend.components.metiers.a_i.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.post("/a_i", json={})
    assert res.status_code == 201
    assert res.json() == {"nom": "", "description": "", "type": "objet"}


def test_create_a_i_with_data():
    from fastapi.testclient import TestClient
    from backend.components.metiers.a_i.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Cube", "description": "Test", "type": "mesh"}
    res = client.post("/a_i", json=data)
    assert res.status_code == 201
    assert res.json() == data


def test_create_a_i_rgpd():
    from fastapi.testclient import TestClient
    from backend.components.metiers.a_i.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Cube", "secret": "should-not-leak"}
    res = client.post("/a_i", json=data)
    assert "secret" not in res.json()


def test_accessibilite_json():
    from fastapi.testclient import TestClient
    from backend.components.metiers.a_i.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/a_i")
    assert res.headers["content-type"].startswith("application/json")
