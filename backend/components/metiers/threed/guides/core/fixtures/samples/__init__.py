# __init__.py – Point d’entrée Python du sous-module samples fixtures
default_sample = None
try:
    from .sample_fixture import sample_fixture_guide
    default_sample = sample_fixture_guide
except ImportError:
    pass
