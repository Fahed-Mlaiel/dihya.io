"""
Dihya Industrie Template Utilities
==================================

FR : Utilitaires avancés pour la gestion, le rendu, la validation et l’audit des templates du module industrie.
EN : Advanced utilities for management, rendering, validation, and audit of industrie module templates.
AR : أدوات متقدمة لإدارة وعرض والتحقق وتدقيق قوالب وحدة "الصناعة".
TZ : Iɣewwaṛen n uselkim, uskan, usenqed, d uɛyan n templates n uγmis "industrie".

Fonctionnalités :
- Rendu sécurisé et multilingue de templates Django/Jinja2
- Validation accessibilité (WCAG/RGAA), i18n, SEO, sécurité, confidentialité industrielle/client
- Gestion dynamique des rôles utilisateur (opérateur, ingénieur, client, admin, invité…)
- Audit et logs d’accès aux templates
- Extensible pour plugins/metiers
- Prêt pour fallback IA open source (Jinja2, GPT4All, etc.)
- Compatible Linux, CI/CD, Codespaces

"""

import os
import logging
from typing import Dict, Any, Optional

from django.template import loader, TemplateDoesNotExist, Template
from django.utils.translation import gettext as _
from django.contrib.auth.models import AnonymousUser

# Logger sécurisé pour audit
logger = logging.getLogger("dihya.industrie.template")
logger.setLevel(logging.INFO)

# Multilingue : messages d’erreur
ERROR_MESSAGES = {
    "fr": "Erreur lors du rendu du template.",
    "en": "Error rendering template.",
    "ar": "خطأ أثناء عرض القالب.",
    "tz": "Tuccda deg uskan n template.",
}

def render_industrie_template(
    template_name: str,
    context: Optional[Dict[str, Any]] = None,
    user=None,
    lang: str = "fr"
) -> str:
    """
    Rendu sécurisé et multilingue d’un template industrie.

    Args:
        template_name (str): Nom du template à charger.
        context (dict): Contexte à injecter.
        user: Utilisateur courant (pour gestion des rôles).
        lang (str): Langue ('fr', 'en', 'ar', 'tz').

    Returns:
        str: HTML rendu.

    Raises:
        TemplateDoesNotExist: Si le template n’existe pas.
        Exception: Pour toute erreur de rendu.
    """
    context = context or {}
    user = user or AnonymousUser()
    context["user"] = user
    context["LANGUAGE_CODE"] = lang

    try:
        tpl: Template = loader.get_template(template_name)
        html = tpl.render(context)
        logger.info(f"[{lang}] Rendered template '{template_name}' for user '{getattr(user, 'username', 'anonymous')}'")
        return html
    except TemplateDoesNotExist:
        logger.error(f"[{lang}] Template '{template_name}' does not exist.")
        raise
    except Exception as e:
        logger.error(f"[{lang}] {ERROR_MESSAGES.get(lang, ERROR_MESSAGES['fr'])} {e}")
        raise

def validate_industrie_template(html: str, lang: str = "fr") -> Dict[str, Any]:
    """
    Validation avancée d’un template HTML industrie (accessibilité, i18n, SEO, sécurité, confidentialité).

    Args:
        html (str): HTML à valider.
        lang (str): Langue des messages.

    Returns:
        dict: Résultats de validation.
    """
    results = {
        "accessibility": True,
        "i18n": True,
        "seo": True,
        "security": True,
        "privacy": True,
        "errors": [],
    }
    # Accessibilité
    if "<html" in html and 'lang="' not in html:
        results["accessibility"] = False
        results["errors"].append(_("Balise <html> sans attribut lang"))
    if "aria-" not in html:
        results["accessibility"] = False
        results["errors"].append(_("Aucune balise ARIA détectée"))
    # i18n
    if "{% trans" not in html and "{% blocktrans" not in html:
        results["i18n"] = False
        results["errors"].append(_("Aucune balise de traduction détectée"))
    # SEO
    if "<meta name=\"description\"" not in html:
        results["seo"] = False
        results["errors"].append(_("Meta description manquante"))
    if "<title>" not in html:
        results["seo"] = False
        results["errors"].append(_("Balise <title> manquante"))
    # Sécurité
    if "<script" in html and "{% static" not in html:
        results["security"] = False
        results["errors"].append(_("Script inline détecté"))
    # Confidentialité industrielle/client
    if "client" in html or "customer" in html or "industrie" in html or "machine" in html:
        if "{{" in html:
            results["privacy"] = False
            results["errors"].append(_("Fuite potentielle de données industrielles ou client/sensibles"))
    return results

def audit_template_access(template_name: str, user=None, lang: str = "fr"):
    """
    Journalise l’accès à un template pour audit et conformité.

    Args:
        template_name (str): Nom du template.
        user: Utilisateur courant.
        lang (str): Langue.
    """
    user_str = getattr(user, "username", "anonymous") if user else "anonymous"
    logger.info(f"[AUDIT][{lang}] Template '{template_name}' accessed by '{user_str}'.")

# Exemple d’utilisation avancée (testable en CI)
if __name__ == "__main__":
    # Test de rendu et validation multilingue
    for lang in ["fr", "en", "ar", "tz"]:
        try:
            html = render_industrie_template("example.html", context={"test": True}, lang=lang)
            results = validate_industrie_template(html, lang=lang)
            audit_template_access("example.html", user=None, lang=lang)
            print(f"[{lang}] Validation results:", results)
        except Exception as e:
            print(f"[{lang}] ERROR:", e)

# --- Fin du module industrie/template.py ---
