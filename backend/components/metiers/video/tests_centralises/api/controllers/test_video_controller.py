# video_controller.test.py – Test ultra avancé pour video_controller.py
# (API Video)
from video.api.controllers.video_controller import (
    get_video,
    create_video,
    update_video,
    delete_video,
)


def test_get_video_exists():
    assert callable(get_video)


def test_create_video_exists():
    assert callable(create_video)


def test_update_video_exists():
    assert callable(update_video)


def test_delete_video_exists():
    assert callable(delete_video)


def test_get_video_nominal():
    # Test nominal : récupération d'une entité existante
    result = get_video(1)
    assert result["id"] == 1
    assert result["name"] == "Cube Ultra"
    assert result["status"] == "active"


def test_get_video_not_found():
    # Test edge case : entité non trouvée
    from video.api.controllers.video_controller import db_find_by_id
    import types

    # Patch temporairement db_find_by_id pour simuler None
    orig = db_find_by_id

    def fake_find_by_id(table, id):
        return None

    import video.api.controllers.video_controller as ctrl

    ctrl.db_find_by_id = fake_find_by_id
    try:
        assert get_video(9999) is None
    finally:
        ctrl.db_find_by_id = orig


def test_create_video_valid():
    # Test création valide
    data = {"name": "Test", "status": "active"}
    result = create_video(data)
    assert result["name"] == "Test"
    assert result["status"] == "active"
    assert "id" in result


def test_create_video_invalid():
    # Test création invalide (nom manquant)
    import pytest

    with pytest.raises(ValueError):
        create_video({"status": "active"})
    with pytest.raises(ValueError):
        create_video({"name": "Test"})
    with pytest.raises(ValueError):
        create_video({"name": 123, "status": "active"})
    with pytest.raises(ValueError):
        create_video({"name": "Test", "status": "foo"})


def test_update_video_nominal():
    # Test mise à jour valide
    data = {"name": "Maj", "status": "inactive"}
    result = update_video(1, data)
    assert result["id"] == 1
    assert result["name"] == "Maj"
    assert result["status"] == "inactive"


def test_delete_video_nominal():
    # Test suppression nominale
    assert delete_video(1) is True
