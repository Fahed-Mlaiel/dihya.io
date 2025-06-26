from transport.api.hooks.hooks import before_action, after_action


def test_before_action():
    assert before_action("create", {"id": 1}) is None


def test_after_action():
    assert after_action("create", {"id": 1}) is None
