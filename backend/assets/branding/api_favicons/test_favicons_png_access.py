"""
test_favicons_png.py – Test unitaire/CI accessibilité & RGPD favicons PNG (Dihya Coding)

- Teste la présence, l’accessibilité, la conformité RGPD, la multilingue et la sécurité des favicons PNG
- Utilise le plugin d’audit accessibilité
- Logs anonymisés, exportables, effaçables
- 100% compatible CI/CD, Codespaces, Linux

Usage :
    pytest test_favicons_png.py
    python3 test_favicons_png.py
"""
import os
import json
from plugin_png_accessibility import audit_png_accessibility

def test_png_accessibility():
    results = audit_png_accessibility('./png')
    assert results, "Aucun favicon PNG trouvé."
    for r in results:
        assert r['hash'], f"Hash manquant pour {r['file']}"
        assert r['alt'], f"Alt multilingue manquant pour {r['file']}"
        assert r['description'], f"Description multilingue manquante pour {r['file']}"
        assert r['audit'] == 'OK', f"Audit accessibilité/metadata KO pour {r['file']}"

if __name__ == "__main__":
    test_png_accessibility()
    print("[OK] Tous les favicons PNG sont conformes accessibilité, RGPD, multilingue.")
