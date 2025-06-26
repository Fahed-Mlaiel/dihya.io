import importlib.util
import os


def find_faq_path():
    cur = os.path.abspath(os.path.dirname(__file__))
    while True:
        candidate = os.path.join(cur, 'docs', 'faq', 'faq.py')
        if os.path.isfile(candidate):
            return candidate
        parent = os.path.dirname(cur)
        if parent == cur:
            raise FileNotFoundError('faq.py introuvable')
        cur = parent


faq_path = find_faq_path()
spec = importlib.util.spec_from_file_location('faq', faq_path)
faq = importlib.util.module_from_spec(spec)
spec.loader.exec_module(faq)
FAQ = faq.FAQ


def test_faq_content():
    assert isinstance(FAQ, list)
    assert any("déployer" in q["q"] for q in FAQ)
    assert any("locale" in q["a"] for q in FAQ)
