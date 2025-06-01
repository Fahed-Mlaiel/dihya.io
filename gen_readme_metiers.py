"""
Dihya - Générateur de README métiers (CSV → Markdown)
Ultra avancé, multilingue, accessible, SEO, prêt CI/CD.

- Génère un README métiers multilingue à partir du CSV de référence.
- Statistiques, sommaire cliquable, détails, accessibilité, SEO, i18n.
- Multilingue (français, anglais, arabe, amazigh) via détection automatique ou paramètre CLI/env.
- Compatible Linux, Codespaces, CI.
- Conforme RGPD : pas de données personnelles traitées.
- Prêt à l'emploi, testé, robuste.

Auteur : Dihya Core Team
Licence : AGPL-3.0
"""

import pandas as pd
import os
import sys
import locale
from datetime import datetime

CSV_PATH = "rapport_metiers.csv"
README_PATH = "README_METIERS.md"
SUPPORTED_LANGS = ["fr", "en", "ar", "tzm"]

def detect_lang():
    lang = os.environ.get("DIHYA_LANG") or locale.getdefaultlocale()[0]
    if lang:
        lang = lang.split("_")[0]
    return lang if lang in SUPPORTED_LANGS else "fr"

def get_labels(lang):
    return {
        "fr": {
            "title": "📊 Synthèse des métiers du projet Dihya",
            "auto": "Ce document est généré automatiquement. **Ne pas modifier à la main.**",
            "stats": "## Statistiques globales",
            "total": "Total métiers listés",
            "present": "Métiers présents dans le projet",
            "expected": "Métiers attendus (CDC)",
            "missing": "Métiers manquants",
            "extra": "Métiers en trop",
            "summary": "## Sommaire",
            "missing_title": "## ❌ Métiers manquants (attendus mais absents)",
            "extra_title": "## ⚠️ Métiers en trop (présents mais non attendus)",
            "detail": "## Détail par métier",
            "present_in_project": "Présent dans le projet",
            "expected_in_cdc": "Attendu dans le CDC",
            "types": "Types détectés",
            "paths": "Chemins",
            "none": "-",
            "generated": "Généré le",
            "lang_notice": "Ce document est disponible en :",
        },
        "en": {
            "title": "📊 Dihya Project Business Roles Summary",
            "auto": "This document is auto-generated. **Do not edit manually.**",
            "stats": "## Global statistics",
            "total": "Total listed roles",
            "present": "Roles present in project",
            "expected": "Expected roles (spec)",
            "missing": "Missing roles",
            "extra": "Extra roles",
            "summary": "## Summary",
            "missing_title": "## ❌ Missing roles (expected but absent)",
            "extra_title": "## ⚠️ Extra roles (present but not expected)",
            "detail": "## Role details",
            "present_in_project": "Present in project",
            "expected_in_cdc": "Expected in spec",
            "types": "Detected types",
            "paths": "Paths",
            "none": "-",
            "generated": "Generated on",
            "lang_notice": "This document is available in:",
        },
        "ar": {
            "title": "📊 ملخص المهن في مشروع ديهيا",
            "auto": "هذا المستند تم إنشاؤه تلقائيًا. **لا تعدل يدويًا.**",
            "stats": "## الإحصائيات العامة",
            "total": "إجمالي المهن المدرجة",
            "present": "المهن الموجودة في المشروع",
            "expected": "المهن المتوقعة (دفتر الشروط)",
            "missing": "المهن المفقودة",
            "extra": "المهن الزائدة",
            "summary": "## المحتوى",
            "missing_title": "## ❌ المهن المفقودة (متوقعة ولكنها غائبة)",
            "extra_title": "## ⚠️ المهن الزائدة (موجودة ولكن غير متوقعة)",
            "detail": "## تفاصيل كل مهنة",
            "present_in_project": "موجود في المشروع",
            "expected_in_cdc": "متوقع في دفتر الشروط",
            "types": "الأنواع المكتشفة",
            "paths": "المسارات",
            "none": "-",
            "generated": "تم الإنشاء في",
            "lang_notice": "هذا المستند متوفر بـ:",
        },
        "tzm": {
            "title": "📊 ⴰⵙⵉⵏⴰⵡⴰⵙ ⵏ ⵉⵎⴻⵏⵉⵙⵏ Dihya",
            "auto": "ⴰⵙⵉⵏⴰⵡⴰⵙ-agi d-ittwasnen s wudem awurman. **Ur ttsnifel ara s ufus.**",
            "stats": "## ⴰⵎⵙⵙⴰⵏ ⴰⴷⴷⴰⵢⴻⵏ",
            "total": "ⴰⵎⵙⵙⴰⵏ ⵏ ⵉⵎⴻⵏⵉⵙⵏ",
            "present": "ⵉⵎⴻⵏⵉⵙⵏ ⴷ ⴰⵙⴳⴳⴰⵙ",
            "expected": "ⵉⵎⴻⵏⵉⵙⵏ ⴰⴷⴷⴰⵢⴻⵏ (CDC)",
            "missing": "ⵉⵎⴻⵏⵉⵙⵏ ⴰⵎⵎⴰⵍⵍⴰⵏ",
            "extra": "ⵉⵎⴻⵏⵉⵙⵏ ⴰⵎⴰⵣⵣⴰⵏ",
            "summary": "## ⴰⵎⵙⵙⴰⵏ",
            "missing_title": "## ❌ ⵉⵎⴻⵏⵉⵙⵏ ⴰⵎⵎⴰⵍⵍⴰⵏ (ⴰⴷⴷⴰⵢⴻⵏ ⴷⴰⵙⴳⴳⴰⵙ ⴷⴰⵎⴰⵍⴰⵏ)",
            "extra_title": "## ⚠️ ⵉⵎⴻⵏⵉⵙⵏ ⴰⵎⴰⵣⵣⴰⵏ (ⴰⴷⴷⴰⵢⴻⵏ ⴷⴰⵙⴳⴳⴰⵙ ⴷⴰⵎⴰⵣⵣⴰⵏ)",
            "detail": "## ⴰⵙⵉⵏⴰⵡⴰⵙ ⴰⴷⴷⴰⵢⴻⵏ",
            "present_in_project": "ⴷ ⴰⵙⴳⴳⴰⵙ",
            "expected_in_cdc": "ⴷ CDC",
            "types": "ⴰⵙⵉⵏⴰⵡⴰⵙ ⴰⴷⴷⴰⵢⴻⵏ",
            "paths": "ⴰⵙⵉⵏⴰⵡⴰⵙ",
            "none": "-",
            "generated": "ⴰⴷⴷⴰⵢ ⴷ",
            "lang_notice": "ⴰⵙⵉⵏⴰⵡⴰⵙ ⴰⴷⴷⴰⵢⴻⵏ ⴷ:",
        }
    }[lang]

def main():
    lang = detect_lang()
    L = get_labels(lang)

    if not os.path.isfile(CSV_PATH):
        print(f"Erreur : {CSV_PATH} introuvable. Lancez d'abord verif_metiers.py.")
        return

    df = pd.read_csv(CSV_PATH)
    total = len(df)
    presents = df['present'].str.lower().eq('oui').sum()
    dans_cdc = df['dans_cdc'].str.lower().eq('oui').sum()
    manquants = df.query("present == 'non' and dans_cdc == 'oui'")
    en_trop = df.query("present == 'oui' and dans_cdc == 'non'")

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(f"# {L['title']}\n\n")
        f.write(f"{L['auto']}\n\n")
        f.write(f"{L['lang_notice']} 🇫🇷 | 🇬🇧 | 🇦🇪 | ⵣ\n\n")
        f.write(f"{L['stats']}\n\n")
        f.write(f"- **{L['total']}** : {total}\n")
        f.write(f"- **{L['present']}** : {presents}\n")
        f.write(f"- **{L['expected']}** : {dans_cdc}\n")
        f.write(f"- **{L['missing']}** : {len(manquants)}\n")
        f.write(f"- **{L['extra']}** : {len(en_trop)}\n")
        f.write(f"- _{L['generated']} {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n\n")

        # Sommaire cliquable
        f.write(f"{L['summary']}\n\n")
        for _, row in df.iterrows():
            anchor = row['metier'].replace('_','-')
            f.write(f"- [{row['metier']}](#{anchor})\n")
        f.write("\n")

        # Métiers manquants
        if len(manquants):
            f.write(f"{L['missing_title']}\n\n")
            for _, row in manquants.iterrows():
                anchor = row['metier'].replace('_','-')
                f.write(f"- [{row['metier']}](#{anchor})\n")
            f.write("\n")

        # Métiers en trop
        if len(en_trop):
            f.write(f"{L['extra_title']}\n\n")
            for _, row in en_trop.iterrows():
                anchor = row['metier'].replace('_','-')
                f.write(f"- [{row['metier']}](#{anchor})\n")
            f.write("\n")

        # Détail par métier
        f.write(f"{L['detail']}\n\n")
        for _, row in df.iterrows():
            anchor = row["metier"].replace("_", "-")
            f.write(f"### <a name=\"{anchor}\"></a> {row['metier']}\n\n")
            f.write(f"- **{L['present_in_project']}** : {'✅' if row['present']=='oui' else '❌'}\n")
            f.write(f"- **{L['expected_in_cdc']}** : {'✅' if row['dans_cdc']=='oui' else '❌'}\n")
            f.write(f"- **{L['types']}** : {row['types'] if pd.notnull(row['types']) else L['none']}\n")
            chemins = row["chemins"] if pd.notnull(row["chemins"]) else ""
            if chemins:
                f.write(f"- **{L['paths']}** :\n")
                for chemin in str(chemins).split("; "):
                    f.write(f"    - `{chemin}`\n")
            f.write("\n")

    print(f"{README_PATH} généré ({lang}).")

if __name__ == "__main__":
    main()
