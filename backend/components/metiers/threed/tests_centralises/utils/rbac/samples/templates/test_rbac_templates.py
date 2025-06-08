from .rbac_templates import render_rbac

def test_render_rbac():
    assert 'admin' in render_rbac('admin')
