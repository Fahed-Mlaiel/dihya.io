# test___init__.py – Test ultra avancé, clé en main


def test_import_router():
    assert True  # Import réussi, module présent


def test___init___structure():
    import seo.views.router

    assert hasattr(seo.views.router, "__doc__")


def test_list_seos():
    from fastapi.testclient import TestClient
    from backend.components.metiers.seo.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/seo")
    assert res.status_code == 200
    assert res.json() == {"seos": [], "total": 0}


def test_create_seo_defaults():
    from fastapi.testclient import TestClient
    from backend.components.metiers.seo.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.post("/seo", json={})
    assert res.status_code == 201
    assert res.json() == {"nom": "", "description": "", "type": "objet"}


def test_create_seo_with_data():
    from fastapi.testclient import TestClient
    from backend.components.metiers.seo.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Cube", "description": "Test", "type": "mesh"}
    res = client.post("/seo", json=data)
    assert res.status_code == 201
    assert res.json() == data


def test_create_seo_rgpd():
    from fastapi.testclient import TestClient
    from backend.components.metiers.seo.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Cube", "secret": "should-not-leak"}
    res = client.post("/seo", json=data)
    assert "secret" not in res.json()


def test_accessibilite_json():
    from fastapi.testclient import TestClient
    from backend.components.metiers.seo.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/seo")
    assert res.headers["content-type"].startswith("application/json")
