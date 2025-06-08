# Ultra advanced RBAC example test (clé en main)
from ..templates import render_rbac

def test_render_superadmin():
    html = render_rbac('superadmin')
    assert 'superadmin' in html
