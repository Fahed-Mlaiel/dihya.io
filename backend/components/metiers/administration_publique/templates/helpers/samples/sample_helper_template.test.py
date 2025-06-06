# sample_helper_template.test.py – Test Python exemple helper template
from .sample_helper_template import sample_helper_template

def test_sample_helper_template_ok():
    assert sample_helper_template({'a': 1}) == {'a': 1, 'helper': True}
    assert sample_helper_template(None) == {'helper': True, 'empty': True}
