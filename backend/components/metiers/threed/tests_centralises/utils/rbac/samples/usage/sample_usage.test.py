from ..templates.rbac_templates import render_rbac

def test_usage():
    assert 'user' in render_rbac('user')
