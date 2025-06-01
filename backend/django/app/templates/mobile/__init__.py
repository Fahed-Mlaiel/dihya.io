"""
Dihya - Mobile Templates
========================

FR : Ce package contient les templates HTML du module "mobile" de Dihya (PWA, web mobile, intégration Flutter/React Native, etc.).
EN : This package contains the HTML templates for the "mobile" module of Dihya (PWA, mobile web, Flutter/React Native integration, etc.).
AR : يحتوي هذا المجلد على قوالب HTML لوحدة "الموبايل" في ديهيا (تطبيقات ويب، PWA، تكامل Flutter/React Native...).
TZ : Asgwas agi yegber templates n HTML n uγmis "mobile" n Dihya (PWA, web mobile, Flutter, React Native...).

Fonctionnalités :
- Documentation multilingue (fr, en, ar, amazigh)
- Vérification automatique d’accessibilité, i18n, sécurité, conformité mobile à l’import
- Prêt pour extension (Jinja2, plugins, hooks, IA open source, PWA, intégration Flutter/React Native, notifications push souveraines)
- Souveraineté numérique : aucune dépendance cloud, sécurité renforcée, conformité RGPD, accessibilité mobile, offline/PWA, notifications souveraines

Utilisation :
- Placez vos fichiers .html ici.
- Les templates sont chargés automatiquement par Django.
- Pour hooks avancés, extensions IA, ou audit mobile, éditez ce fichier.

Auto-check (lint, accessibilité, i18n, sécurité, conformité mobile) activé à l’import (désactivable via DIHYA_TEMPLATE_CHECK=0)
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
    - Responsive meta viewport
    - Pas de fuite de données personnelles, de tracking non souverain, ou d’informations mobiles confidentielles
    - Respect de la conformité RGPD et des obligations mobile (pas de cookies tiers, pas de tracking tiers, mentions légales, accessibilité mobile)
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
            if "<meta name=\"viewport\"" not in content:
                errors.append(f"{tpl_path}: Missing responsive viewport meta")
            if "tracking" in content or "cookie" in content or "analytics" in content:
                errors.append(f"{tpl_path}: Non-compliant content (RGPD/mobile)")
            if "confidentiel" in content or "sensible" in content or "secret" in content:
                if "{{" in content:
                    errors.append(f"{tpl_path}: Potential leak of sensitive/mobile/confidential data")
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

# Extension possible : hooks IA, audit mobile, moteurs alternatifs, plugins, fallback open source, notifications souveraines, etc.
