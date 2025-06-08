# Ultra advanced RBAC template test (clé en main)
from .rbac_templates import render_rbac

def test_render_compliance():
    assert 'compliance' in render_rbac('compliance')
