# ⚡ Dihya Energy Templates

---

## 🇫🇷 Présentation

Ce dossier contient les **templates métiers pour l’énergie** de Dihya, prêts à l’emploi, extensibles, sécurisés, multilingues et souverains.
Ajoutez, découvrez et personnalisez des modèles pour factures, relevés, production, consommation, IA, plugins, etc.

- **Sécurité** : Aucun code exécutable à l’import, audit automatique, conformité RGPD, pas de tracking.
- **Extensible** : Ajoutez vos propres templates, assets, scripts, plugins, IA, etc.
- **Multilingue** : Prise en charge native du français, anglais, arabe, amazigh.
- **Souveraineté numérique** : 100% open source, aucune dépendance cloud propriétaire.
- **Accessibilité** : Compatible avec les outils d’accessibilité, structuration ARIA, SEO-ready.

---

## 🇬🇧 Overview

This folder contains **business energy templates** for Dihya: ready-to-use, extensible, secure, multilingual, and sovereign.
Add, discover, and customize models for invoices, meter readings, production, consumption, AI, plugins, and more.

- **Security**: No executable code on import, automatic audit, GDPR compliance, no tracking.
- **Extensible**: Add your own templates, assets, scripts, plugins, AI, etc.
- **Multilingual**: Native support for French, English, Arabic, Amazigh.
- **Digital sovereignty**: 100% open source, no proprietary cloud dependency.
- **Accessibility**: Compatible with accessibility tools, ARIA structure, SEO-ready.

---

## 🇦🇪 نظرة عامة

يحتوي هذا المجلد على **قوالب الطاقة** الجاهزة والقابلة للتوسعة والآمنة ومتعددة اللغات وذات سيادة رقمية.
يمكنك إضافة واكتشاف وتخصيص النماذج للفواتير، القراءات، الإنتاج، الاستهلاك، الذكاء الاصطناعي، الإضافات، وأكثر.

- **الأمان**: لا يوجد كود قابل للتنفيذ عند الاستيراد، تدقيق تلقائي، متوافق مع GDPR، بدون تتبع.
- **قابلية التوسعة**: أضف قوالبك وأصولك وإضافاتك وذكاءك الاصطناعي.
- **متعدد اللغات**: دعم أصلي للفرنسية، الإنجليزية، الأمازيغية، العربية.
- **السيادة الرقمية**: مفتوح المصدر بالكامل، بدون اعتماد على سحابة خاصة.
- **إتاحة الوصول**: متوافق مع أدوات الوصول، بنية ARIA، جاهز لتحسين محركات البحث.

---

## ⵣ Aglam n tazwart n tazwart

Agan ameslay agi yegber **templates n tazrawt n tazwart** n Dihya, yellan-d-d awid, amatu, amatu, multilingual, tasertit n digital.
Tzemreḍ ad ternuḍ, ad ttwaliḍ, ad tzemreḍ templates n factures, relevés, production, consommation, IA, plugins, d wayen-nniḍen.

- **Amatu**: Ulac code ixeddem s wudem automatic, audit, GDPR, ulac tracking.
- **Amatu**: Rnu templates, assets, scripts, plugins, IA, d wayen-nniḍen.
- **Multilingual**: Tamazight, Tafrantsist, Taglizit, Taɛrabt.
- **Tasertit n digital**: 100% open source, ulac cloud proprietary.
- **Accessibility**: Yeddu s yirna n accessibility, ARIA, SEO.

---

## 🚀 Utilisation / Usage

### Découvrir les templates disponibles

```python
from . import discover_energy_templates

print(discover_energy_templates(lang="fr"))
```

### Ajouter un template

1. Placez votre fichier (ex: `facture_fr.yaml`, `releve_en.json`, `production_ar.py`) dans ce dossier.
2. Il sera automatiquement détecté par `discover_energy_templates`.

### Exemple de template YAML

```yaml
# filepath: /workspaces/Dihya/Dihya/backend/django/app/templates/energie/facture_fr.yaml
type: facture
lang: fr
structure:
  - champ: numero_facture
    label: "Numéro de facture"
  - champ: date
    label: "Date"
  - champ: montant
    label: "Montant total"
meta:
  description:
    fr: "Template de facture énergie standard"
    en: "Standard energy invoice template"
    ar: "قالب فاتورة طاقة قياسي"
    tz: "Template n tazrawt n facture n tazwart"
  roles: ["admin", "technicien", "client"]
  accessibility: {aria-label: "Facture énergie", seo: true}
  version: "1.0.0"
  license: "AGPL-3.0-or-later"
```

---

## 🛡️ Sécurité & Souveraineté

- Aucun code exécutable à l’import.
- Audit automatique via CI/CD (voir `.github/workflows/ci.yml`).
- RGPD, accessibilité, SEO, multilingue, open source only.

---

## 🧩 Plugins & IA

- Ajoutez vos plugins Python, scripts IA, ou assets dans ce dossier.
- Voir la documentation dans `/docs/plugins.md` et `/docs/ia.md`.

---

## 🧪 Tests

- Couverture 100% via `pytest` et `pytest-cov`.
- Tests d’intégration et E2E dans `/tests/energie/`.

---

## 🌍 Multilingue

- Tous les templates et assets doivent indiquer la langue (`lang: fr`, `lang: en`, etc.).
- Voir `/docs/i18n.md` pour la gestion avancée.

---

## 🤝 Contribution

- Fork, PR, audit, tests, docs, traduction bienvenus !
- Respectez la charte souveraineté numérique et sécurité.

---

## 📚 Documentation

- [Guide complet (fr)](../../../../docs/README.fr.md)
- [Full guide (en)](../../../../docs/README.en.md)
- [دليل كامل (ar)](../../../../docs/README.ar.md)
- [Aglam umenzu (tz)](../../../../docs/README.tz.md)

---

© 2025 Dihya – Open Source, souverain, multilingue, inclusif.
