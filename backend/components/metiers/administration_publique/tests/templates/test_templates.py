import os, glob
import jinja2
import pytest

def get_templates_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '../../templates/templates'))

def list_templates():
    dir = get_templates_dir()
    return [f for f in os.listdir(dir) if f.endswith('.j2') or f.endswith('.html')]

def test_templates_exist():
    templates = list_templates()
    assert len(templates) > 0
    for tpl in templates:
        assert tpl.endswith('.j2') or tpl.endswith('.html')

def test_template_rendering():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(get_templates_dir()))
    for tpl_name in list_templates():
        template = env.get_template(tpl_name)
        # Dummy context for rendering
        context = {k: 'test' for k in ['score','details','recommandations','message','date','service','description','date_export','contenu','type','resultat']}
        rendered = template.render(**context)
        assert isinstance(rendered, str)
        assert len(rendered) > 0
