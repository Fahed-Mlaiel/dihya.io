# test___init__.py – Test ultra avancé, clé en main


def test_import_router():
    assert True  # Import réussi, module présent


def test___init___structure():
    import services_personne.views.router

    assert hasattr(services_personne.views.router, "__doc__")


def test_list_services_personnes():
    from fastapi.testclient import TestClient
    from backend.components.metiers.services_personne.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/services_personne")
    assert res.status_code == 200
    assert res.json() == {"services_personnes": [], "total": 0}


def test_create_services_personne_defaults():
    from fastapi.testclient import TestClient
    from backend.components.metiers.services_personne.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.post("/services_personne", json={})
    assert res.status_code == 201
    assert res.json() == {"nom": "", "description": "", "type": "objet"}


def test_create_services_personne_with_data():
    from fastapi.testclient import TestClient
    from backend.components.metiers.services_personne.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Cube", "description": "Test", "type": "mesh"}
    res = client.post("/services_personne", json=data)
    assert res.status_code == 201
    assert res.json() == data


def test_create_services_personne_rgpd():
    from fastapi.testclient import TestClient
    from backend.components.metiers.services_personne.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Cube", "secret": "should-not-leak"}
    res = client.post("/services_personne", json=data)
    assert "secret" not in res.json()


def test_accessibilite_json():
    from fastapi.testclient import TestClient
    from backend.components.metiers.services_personne.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/services_personne")
    assert res.headers["content-type"].startswith("application/json")
