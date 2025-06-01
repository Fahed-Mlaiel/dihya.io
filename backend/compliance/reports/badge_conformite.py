"""
Module de génération de badge SVG de conformité dynamique, accessible, multilingue, CI/CD, RGPD, audit, plugins, extensible.
"""
from typing import Literal, Optional
import datetime

LANGS = {
    "fr": {"label": "Conforme", "desc": "Badge de conformité RGPD et sécurité"},
    "en": {"label": "Compliant", "desc": "Compliance badge (GDPR, security)"},
    "ar": {"label": "متوافق", "desc": "شارة الامتثال (اللائحة العامة لحماية البيانات، الأمان)"},
    "ber": {"label": "ⴰⵙⵉⵏⴼⴰⵡ", "desc": "ⴱⴰⴷⵊ ⴷ ⴰⵙⵉⵏⴼⴰⵡ (RGPD, ⴰⵙⵉⵏⴼⴰⵡ)"},
    "de": {"label": "Konform", "desc": "Konformitätsabzeichen (DSGVO, Sicherheit)"},
    "zh": {"label": "合规", "desc": "合规徽章（GDPR，安全）"},
    "ja": {"label": "準拠", "desc": "コンプライアンスバッジ（GDPR、セキュリティ）"},
    "ko": {"label": "준수", "desc": "준수 배지(GDPR, 보안)"},
    "nl": {"label": "Conform", "desc": "Conformiteitsbadge (AVG, beveiliging)"},
    "he": {"label": "תואם", "desc": "תג תאימות (GDPR, אבטחה)"},
    "fa": {"label": "مطابق", "desc": "نشان انطباق (GDPR، امنیت)"},
    "hi": {"label": "अनुपालन", "desc": "अनुपालन बैज (GDPR, सुरक्षा)"},
    "es": {"label": "Conforme", "desc": "Insignia de conformidad (RGPD, seguridad)"},
}

STATE_COLORS = {
    "conforme": "#2ecc40",
    "non conforme": "#ff4136",
    "audit": "#ffdc00",
    "en attente": "#0074d9",
}


def generer_badge_conformite(
    etat: Literal["conforme", "non conforme", "audit", "en attente"] = "conforme",
    langue: str = "fr",
    date: Optional[str] = None,
    ci: bool = True,
    plugin: Optional[str] = None,
    acces_aria: bool = True,
) -> str:
    """
    Génère un badge SVG dynamique de conformité (accessibilité, multilingue, CI, RGPD, plugins).
    :param etat: État de conformité ("conforme", "non conforme", "audit", "en attente")
    :param langue: Code langue (fr, en, ar, ber, de, zh, ja, ko, nl, he, fa, hi, es)
    :param date: Date d’émission (ISO8601), défaut = aujourd’hui
    :param ci: Afficher l’icône CI/CD
    :param plugin: Nom du plugin métier (optionnel)
    :param acces_aria: Inclure ARIA/desc pour accessibilité
    :return: SVG string
    """
    l = LANGS.get(langue, LANGS["fr"])
    color = STATE_COLORS.get(etat, STATE_COLORS["conforme"])
    date_str = date or datetime.date.today().isoformat()
    plugin_str = f" | {plugin}" if plugin else ""
    ci_str = (
        '<g aria-label="CI/CD" role="img"><circle cx="110" cy="12" r="6" fill="#0074d9"/><text x="110" y="16" font-size="10" fill="#fff" font-family="Arial" text-anchor="middle">CI</text></g>'
        if ci else ""
    )
    aria = (
        f'aria-label="{l["desc"]} – {etat}{plugin_str} – {date_str}" role="img"'
        if acces_aria else "role=\"img\""
    )
    # Si acces_aria est False, ne pas inclure aria-label du tout
    if not acces_aria:
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="140" height="28" viewBox="0 0 140 28" role="img">
  <title>{l["label"]} – Dihya Compliance</title>
  <rect rx="6" width="140" height="28" fill="{color}"/>
  <text x="16" y="18" font-size="14" fill="#fff" font-family="Arial" font-weight="bold">{l["label"]}</text>
  <text x="70" y="18" font-size="10" fill="#fff" font-family="Arial">{etat.capitalize()}</text>
  <text x="70" y="26" font-size="8" fill="#fff" font-family="Arial">{date_str}{plugin_str}</text>
  {ci_str}
  <g>
    <rect x="120" y="4" width="16" height="16" rx="4" fill="#222"/>
    <text x="128" y="16" font-size="12" fill="#fff" font-family="Arial" text-anchor="middle">✓</text>
  </g>
</svg>'''
        return svg

    desc = (
        f'<desc>{l["desc"]} – {etat}{plugin_str} – {date_str}</desc>'
        if acces_aria else ""
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="140" height="28" viewBox="0 0 140 28" {aria}>
  <title>{l["label"]} – Dihya Compliance</title>
  {desc}
  <rect rx="6" width="140" height="28" fill="{color}"/>
  <text x="16" y="18" font-size="14" fill="#fff" font-family="Arial" font-weight="bold">{l["label"]}</text>
  <text x="70" y="18" font-size="10" fill="#fff" font-family="Arial">{etat.capitalize()}</text>
  <text x="70" y="26" font-size="8" fill="#fff" font-family="Arial">{date_str}{plugin_str}</text>
  {ci_str}
  <g>
    <rect x="120" y="4" width="16" height="16" rx="4" fill="#222"/>
    <text x="128" y="16" font-size="12" fill="#fff" font-family="Arial" text-anchor="middle">✓</text>
  </g>
</svg>'''
    return svg
