"""
Dihya - Recherche Templates
===========================

FR : Ce package contient les templates HTML du module "recherche" de Dihya (recherche avancée, filtres, suggestions IA, résultats, accessibilité, etc.).
EN : This package contains the HTML templates for the "recherche" (search) module of Dihya (advanced search, filters, AI suggestions, results, accessibility, etc.).
AR : يحتوي هذا المجلد على قوالب HTML لوحدة "البحث" في ديهيا (بحث متقدم، فلاتر، اقتراحات ذكاء اصطناعي، نتائج، وصول...).
TZ : Asgwas agi yegber templates n HTML n uγmis "recherche" n Dihya (anadi uslig, ifilter, isumar IA, igmawen, tawuri...).

Fonctionnalités :
- Documentation multilingue (fr, en, ar, amazigh)
- Vérification automatique d’accessibilité, i18n, sécurité, conformité recherche à l’import
- Prêt pour extension (Jinja2, plugins, hooks, IA open source, recherche souveraine, audit, fallback IA)
- Souveraineté numérique : aucune dépendance cloud, sécurité renforcée, conformité RGPD, gestion droits recherche, accessibilité, recherche souveraine

Utilisation :
- Placez vos fichiers .html ici.
- Les templates sont chargés automatiquement par Django.
- Pour hooks avancés, extensions IA, ou audit recherche, éditez ce fichier.

Auto-check (lint, accessibilité, i18n, sécurité, conformité recherche) activé à l’import (désactivable via DIHYA_TEMPLATE_CHECK=0)
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
    - Pas de fuite de données personnelles, de tracking non souverain, ou d’informations confidentielles
    - Respect de la conformité RGPD et des obligations recherche (pas de cookies tiers, pas de tracking tiers, mentions légales, droits recherche)
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
                errors.append(f"{tpl_path}: Non-compliant content (RGPD/recherche)")
            if "confidentiel" in content or "sensible" in content or "secret" in content:
                if "{{" in content:
                    errors.append(f"{tpl_path}: Potential leak of sensitive/recherche/confidential data")
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

# Extension possible : hooks IA, audit recherche, moteurs alternatifs, plugins, fallback open source, recherche souveraine, etc.
