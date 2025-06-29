from juridique.api.rgpd.rgpd import rgpd_sanitize


def test___init___sanitize():
    entity = {"id": 1, "name": "Test"}
    result = rgpd_sanitize(entity)
    assert result == entity
