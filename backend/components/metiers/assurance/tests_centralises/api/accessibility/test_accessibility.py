from assurance.api.accessibility.accessibility import check_accessibility


class TestAccessibility:
    def test_accessibility_basic(self):
        entity = {"label": "Test"}
        assert check_accessibility(entity) is True
        assert check_accessibility({}) is False
        assert check_accessibility(None) is False

    def test_accessibility_advanced(self):
        entity = {"alt": "Alternative"}
        assert check_accessibility(entity) is True
        # Cas limites
        assert check_accessibility({"foo": "bar"}) is False
        assert check_accessibility({"label": ""}) is True
