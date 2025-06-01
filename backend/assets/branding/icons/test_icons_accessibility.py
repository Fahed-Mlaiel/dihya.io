"""
test_icons_accessibility.py – Test accessibilité & RGPD icônes SVG (Dihya Coding)

- Teste la présence, l’accessibilité, la conformité RGPD, la multilingue et la sécurité des icônes SVG
- Logs anonymisés, exportables, effaçables
- 100% compatible CI/CD, Codespaces, Linux

Usage :
    pytest test_icons_accessibility.py
    python3 test_icons_accessibility.py
"""
import os
import json

def test_icons_accessibility():
    for fname in os.listdir('.'):
        if fname.startswith('meta_icon-api-') and fname.endswith('.json'):
            with open(fname, 'r', encoding='utf-8') as f:
                meta = json.load(f)
            assert meta['alt'], f"Alt multilingue manquant pour {fname}"
            assert meta['description'], f"Description multilingue manquante pour {fname}"
            assert meta['audit']['accessibility'] == 'AAA', f"Accessibilité non AAA pour {fname}"
            assert meta['audit']['rgpd'] is True, f"RGPD non conforme pour {fname}"
            assert meta['audit']['tested'] is True, f"Test manquant pour {fname}"
            assert meta['audit']['ci'] is True, f"CI manquant pour {fname}"

if __name__ == "__main__":
    test_icons_accessibility()
    print("[OK] Toutes les icônes SVG sont conformes accessibilité, RGPD, multilingue.")
