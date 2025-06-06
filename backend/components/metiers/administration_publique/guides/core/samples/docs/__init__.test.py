# __init__.test.py – Test d'import du point d'entrée Python docs (guides/core/samples/docs)
def test_import_docs_init():
    import importlib
    docs = importlib.import_module('backend.components.metiers.threed.guides.core.samples.docs')
    assert docs.sample_guide_doc is not None
