# ai_core.test.py
# Tests unitaires Python pour ai_core
from .ai_core import predict_ai

def test_predict_ai():
    assert 'Prédiction pour: Texte' in predict_ai('Texte')

def test_predict_ai_empty():
    assert predict_ai('') == '[AI-CORE] Entrée vide'
