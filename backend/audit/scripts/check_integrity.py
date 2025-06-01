"""
Dihya – Script d’Audit d’Intégrité Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)
--------------------------------------------------------------------------------------------------
- Vérifie l’intégrité SHA-256 de tous les assets backend (modèles, datasets, configs, clés publiques…)
- Génère un rapport exhaustif (console + CSV + JSON), prêt pour audit RGPD/NIS2, CI/CD, production
- Compatible Linux, Codespaces, cloud souverain, multi-stack (Node, Python, plugins)
- Multilingue (fr, en, ar, tzm), logs, accessibilité, documentation claire
- Prêt à l’emploi, robuste, testé, sans fail CI/lint

🇫🇷 Script d’audit d’intégrité des assets backend (sécurité, souveraineté, multilingue)
🇬🇧 Backend assets integrity audit script (security, sovereignty, multilingual)
🇦🇪 برنامج تدقيق سلامة أصول الباكند (الأمان، السيادة، متعدد اللغات)
ⵣ Asnul n audit n tazwart n backend assets (amatu, fallback, multilingual)
"""

import os
import hashlib
import csv
import json
import argparse
from datetime import datetime

ASSETS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../assets'))

LANGS = {
    "fr": {
        "start": "🔍 Vérification d’intégrité des assets backend Dihya…",
        "ok": "✅ Intégrité vérifiée pour tous les assets.",
        "fail": "❌ Intégrité compromise pour :",
        "report": "Rapport généré :",
        "file": "Fichier",
        "hash": "SHA-256",
        "status": "Statut",
        "missing": "Manquant",
        "corrupt": "Corrompu",
        "valid": "Valide"
    },
    "en": {
        "start": "🔍 Checking Dihya backend assets integrity…",
        "ok": "✅ All assets integrity verified.",
        "fail": "❌ Integrity compromised for:",
        "report": "Report generated:",
        "file": "File",
        "hash": "SHA-256",
        "status": "Status",
        "missing": "Missing",
        "corrupt": "Corrupted",
        "valid": "Valid"
    },
    "ar": {
        "start": "🔍 التحقق من سلامة أصول الباكند Dihya…",
        "ok": "✅ تم التحقق من سلامة جميع الأصول.",
        "fail": "❌ سلامة الأصول مفقودة لـ:",
        "report": "تم إنشاء التقرير:",
        "file": "ملف",
        "hash": "SHA-256",
        "status": "الحالة",
        "missing": "مفقود",
        "corrupt": "تالف",
        "valid": "سليم"
    },
    "tzm": {
        "start": "🔍 Asnul n tazwart n backend assets Dihya…",
        "ok": "✅ Akk assets ttwarnan.",
        "fail": "❌ Integrity ur ttwaf ara i:",
        "report": "Rapport yettwarnan:",
        "file": "Afaylu",
        "hash": "SHA-256",
        "status": "Addad",
        "missing": "Ulac",
        "corrupt": "Yettwasel",
        "valid": "Yettwasen"
    }
}

def sha256sum(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def walk_assets(root):
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            yield os.path.relpath(os.path.join(dirpath, f), root)

def load_reference_hashes(ref_file):
    if not os.path.isfile(ref_file):
        return {}
    with open(ref_file, encoding="utf-8") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(
        description="Audit d’intégrité des assets backend Dihya (SHA-256, multilingue, CI/CD-ready)"
    )
    parser.add_argument("--lang", type=str, default="fr", choices=LANGS.keys(), help="Langue du rapport")
    parser.add_argument("--ref", type=str, default="assets_hashes.json", help="Fichier de référence des hashes SHA-256")
    parser.add_argument("--csv", action="store_true", help="Exporter le rapport au format CSV")
    parser.add_argument("--json", action="store_true", help="Exporter le rapport au format JSON")
    args = parser.parse_args()

    L = LANGS[args.lang]
    print(L["start"])

    ref_hashes = load_reference_hashes(os.path.join(ASSETS_ROOT, args.ref))
    results = []
    compromised = []

    for rel_path in walk_assets(ASSETS_ROOT):
        abs_path = os.path.join(ASSETS_ROOT, rel_path)
        hash_ = sha256sum(abs_path)
        ref_hash = ref_hashes.get(rel_path)
        status = L["valid"] if (ref_hash and hash_ == ref_hash) else (L["corrupt"] if ref_hash else L["missing"])
        results.append({
            L["file"]: rel_path,
            L["hash"]: hash_,
            L["status"]: status
        })
        if status != L["valid"]:
            compromised.append(rel_path)

    if compromised:
        print(f"{L['fail']} {', '.join(compromised)}")
    else:
        print(L["ok"])

    # Export CSV
    if args.csv:
        csv_path = os.path.join(ASSETS_ROOT, "integrity_report.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[L["file"], L["hash"], L["status"]])
            writer.writeheader()
            for row in results:
                writer.writerow(row)
        print(f"{L['report']} {csv_path}")

    # Export JSON
    if args.json:
        json_path = os.path.join(ASSETS_ROOT, "integrity_report.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"{L['report']} {json_path}")

if __name__ == "__main__":
    main()
