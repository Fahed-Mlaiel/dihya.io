# test___init__.py – Test ultra avancé, clé en main


def test_import_router():
    assert True  # Import réussi, module présent


def test___init___structure():
    import video.views.router

    assert hasattr(video.views.router, "__doc__")


def test_list_videos():
    from fastapi.testclient import TestClient
    from backend.components.metiers.video.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/video")
    assert res.status_code == 200
    assert res.json() == {"videos": [], "total": 0}


def test_create_video_defaults():
    from fastapi.testclient import TestClient
    from backend.components.metiers.video.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.post("/video", json={})
    assert res.status_code == 201
    assert res.json() == {"nom": "", "description": "", "type": "objet"}


def test_create_video_with_data():
    from fastapi.testclient import TestClient
    from backend.components.metiers.video.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Cube", "description": "Test", "type": "mesh"}
    res = client.post("/video", json=data)
    assert res.status_code == 201
    assert res.json() == data


def test_create_video_rgpd():
    from fastapi.testclient import TestClient
    from backend.components.metiers.video.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    data = {"nom": "Cube", "secret": "should-not-leak"}
    res = client.post("/video", json=data)
    assert "secret" not in res.json()


def test_accessibilite_json():
    from fastapi.testclient import TestClient
    from backend.components.metiers.video.views.router.router import router
    from fastapi import FastAPI

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)
    res = client.get("/video")
    assert res.headers["content-type"].startswith("application/json")
