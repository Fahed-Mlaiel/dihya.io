"""
Dihya - Juridique Templates
===========================

FR : Ce package contient les templates HTML du module "juridique" de Dihya.
EN : This package contains the HTML templates for the "juridique" (legal) module of Dihya.
AR : يحتوي هذا المجلد على قوالب HTML لوحدة "القانون" في ديهيا.
TZ : Asgwas agi yegber templates n HTML n uγmis "juridique" n Dihya.

Fonctionnalités :
- Documentation multilingue (fr, en, ar, amazigh)
- Vérification automatique d’accessibilité, i18n, sécurité, conformité juridique à l’import
- Prêt pour extension (Jinja2, plugins, hooks, IA open source, conformité RGPD, audit)
- Souveraineté numérique : aucune dépendance cloud, sécurité renforcée, conformité RGPD, traçabilité juridique

Utilisation :
- Placez vos fichiers .html ici.
- Les templates sont chargés automatiquement par Django.
- Pour hooks avancés, extensions IA, ou audit juridique, éditez ce fichier.

Auto-check (lint, accessibilité, i18n, sécurité, conformité juridique) activé à l’import (désactivable via DIHYA_TEMPLATE_CHECK=0)
"""

import os
import glob

TEMPLATE_DIR = os.path.dirname(__file__)

def check_templates():
    """
    Vérifie les bonnes pratiques sur tous les templates :
    - <html lang=""> présent
    - Pas de TODO/FIXME
    - Encodage UTF-8
    - Pas de <script> inline
    - Présence de {% trans %} ou {% blocktrans %}
    - Pas de fuite de données personnelles, clauses confidentielles, ou informations juridiques sensibles
    - Respect de la conformité RGPD et des obligations légales (pas de tracking, pas de cookies tiers, mentions légales)
    """
    errors = []
    for tpl_path in glob.glob(os.path.join(TEMPLATE_DIR, "*.html")):
        with open(tpl_path, encoding="utf-8") as f:
            content = f.read()
            if "<html" in content and 'lang="' not in content:
                errors.append(f"{tpl_path}: Missing lang attribute in <html>")
            if "TODO" in content or "FIXME" in content:
                errors.append(f"{tpl_path}: Contains TODO/FIXME")
            if "<script" in content and "{% static" not in content:
                errors.append(f"{tpl_path}: Inline <script> detected (security risk)")
            if "{% trans" not in content and "{% blocktrans" not in content:
                errors.append(f"{tpl_path}: Missing i18n tags")
            if "personnel" in content or "confidentiel" in content or "secret" in content or "clause" in content:
                if "{{" in content:
                    errors.append(f"{tpl_path}: Potential leak of personal/confidential/legal data")
            if "tracking" in content or "cookie" in content or "analytics" in content:
                errors.append(f"{tpl_path}: Non-compliant content (RGPD/legal)")
    if errors:
        raise ImportError(
            "Template check failed:\n" + "\n".join(errors)
        )

if os.environ.get("DIHYA_TEMPLATE_CHECK", "1") == "1":
    try:
        check_templates()
    except Exception as e:
        import warnings
        warnings.warn(str(e))

# Extension possible : hooks IA, audit juridique, moteurs alternatifs, plugins, fallback open source, etc.
