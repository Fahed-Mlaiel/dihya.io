from .template_threed import render_threed_template

def test_render_threed_template():
    assert 'Test' in render_threed_template({'title': 'Test'})
