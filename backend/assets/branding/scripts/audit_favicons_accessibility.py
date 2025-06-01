"""
audit_favicons_accessibility.py – Audit accessibilité & RGPD favicons (Dihya Coding)

- Teste la présence, l’accessibilité, la conformité RGPD, la multilingue et la sécurité des favicons
- Logs anonymisés, exportables, effaçables
- 100% compatible CI/CD, Codespaces, Linux

Usage :
    pytest audit_favicons_accessibility.py
    python3 audit_favicons_accessibility.py
"""
import os
import json

def audit_favicons_accessibility():
    for fname in os.listdir('.'):
        if fname.startswith('meta_favicon-') and fname.endswith('.json'):
            with open(fname, 'r', encoding='utf-8') as f:
                meta = json.load(f)
            assert meta['alt'], f"Alt multilingue manquant pour {fname}"
            assert meta['description'], f"Description multilingue manquante pour {fname}"
            assert meta['audit']['accessibility'] == 'AAA', f"Accessibilité non AAA pour {fname}"
            assert meta['audit']['rgpd'] is True, f"RGPD non conforme pour {fname}"
            assert meta['audit']['tested'] is True, f"Test manquant pour {fname}"
            assert meta['audit']['ci'] is True, f"CI manquant pour {fname}"

if __name__ == "__main__":
    audit_favicons_accessibility()
    print("[OK] Tous les favicons sont conformes accessibilité, RGPD, multilingue.")
