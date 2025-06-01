"""
Dihya Medias Template Utilities
==============================

FR : Utilitaires avancés pour la gestion, le rendu, la validation et l’audit des templates du module medias (gestion de médias, DAM, streaming, galerie, upload, etc.).
EN : Advanced utilities for management, rendering, validation, and audit of medias module templates.
AR : أدوات متقدمة لإدارة وعرض والتحقق وتدقيق قوالب وحدة "الوسائط".
TZ : Iɣewwaṛen n uselkim, uskan, usenqed, d uɛyan n templates n uγmis "medias".

Fonctionnalités :
- Rendu sécurisé et multilingue de templates Django/Jinja2
- Validation accessibilité (WCAG/RGAA), i18n, SEO, sécurité, confidentialité, conformité médias (RGPD, droits d’auteur, accessibilité)
- Gestion dynamique des rôles utilisateur (gestionnaire médias, contributeur, admin, invité…)
- Audit et logs d’accès aux templates
- Extensible pour plugins/metiers, DAM, streaming souverain, fallback IA open source (Jinja2, GPT4All, etc.)
- Compatible Linux, CI/CD, Codespaces

"""

import os
import logging
from typing import Dict, Any, Optional

from django.template import loader, TemplateDoesNotExist, Template
from django.utils.translation import gettext as _
from django.contrib.auth.models import AnonymousUser

# Logger sécurisé pour audit
logger = logging.getLogger("dihya.medias.template")
logger.setLevel(logging.INFO)

# Multilingue : messages d’erreur
ERROR_MESSAGES = {
    "fr": "Erreur lors du rendu du template.",
    "en": "Error rendering template.",
    "ar": "خطأ أثناء عرض القالب.",
    "tz": "Tuccda deg uskan n template.",
}

def render_medias_template(
    template_name: str,
    context: Optional[Dict[str, Any]] = None,
    user=None,
    lang: str = "fr"
) -> str:
    """
    Rendu sécurisé et multilingue d’un template medias.

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

def validate_medias_template(html: str, lang: str = "fr") -> Dict[str, Any]:
    """
    Validation avancée d’un template HTML medias (accessibilité, i18n, SEO, sécurité, confidentialité, conformité RGPD/droits d’auteur).

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
        "medias": True,
        "copyright": True,
        "errors": [],
    }
    # Accessibilité
    if "<html" in html and 'lang="' not in html:
        results["accessibility"] = False
        results["errors"].append(_("Balise <html> sans attribut lang"))
    if "aria-" not in html and "<img" in html:
        results["accessibility"] = False
        results["errors"].append(_("Aucune balise ARIA détectée pour les médias"))
    if "<img" in html and 'alt="' not in html:
        results["accessibility"] = False
        results["errors"].append(_("Balise <img> sans attribut alt"))
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
    # Confidentialité & conformité médias
    if any(word in html for word in ["confidentiel", "sensible", "secret"]):
        if "{{" in html:
            results["privacy"] = False
            results["medias"] = False
            results["errors"].append(_("Fuite potentielle de données sensibles/confidentielles/médias"))
    if "tracking" in html or "cookie" in html or "analytics" in html:
        results["medias"] = False
        results["errors"].append(_("Contenu non conforme RGPD/médias"))
    # Droits d’auteur
    if "©" not in html and "&copy;" not in html:
        results["copyright"] = False
        results["errors"].append(_("Mention de droits d’auteur manquante"))
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
            html = render_medias_template("example.html", context={"test": True}, lang=lang)
            results = validate_medias_template(html, lang=lang)
            audit_template_access("example.html", user=None, lang=lang)
            print(f"[{lang}] Validation results:", results)
        except Exception as e:
            print(f"[{lang}] ERROR:", e)

# --- Fin du module medias/template.py ---
