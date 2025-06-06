import os, glob
import jinja2
import pytest

def get_templates_dir():
    return os.path.dirname(__file__).replace('tests', 'templates')

def list_templates():
    return [f for f in glob.glob(os.path.join(get_templates_dir(), '*.j2'))]

def test_templates_exist():
    templates = list_templates()
    assert len(templates) > 0
    for tpl in templates:
        assert tpl.endswith('.j2')

def test_template_rendering():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(get_templates_dir()))
    for tpl_name in os.listdir(get_templates_dir()):
        if tpl_name.endswith('.j2'):
            template = env.get_template(tpl_name)
            # Dummy context for rendering
            context = {k: 'test' for k in ['score','details','recommandations','message','date','service','description','date_export','contenu','type','resultat']}
            rendered = template.render(**context)
            assert isinstance(rendered, str)
            assert len(rendered) > 0
