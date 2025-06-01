# 🌍 Locales – Dihya Coding

Ce dossier regroupe toutes les traductions, dialectes et fichiers de langues utilisés dans Dihya Coding pour garantir une expérience multilingue, inclusive, moderne et conforme RGPD.  
Chaque fichier vise : design moderne, accessibilité, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Offrir une expérience utilisateur multilingue et locale (arabe, berbère, français, anglais, dialectes…)
- Garantir la conformité RGPD, la sécurité et l’auditabilité des contenus traduits
- Faciliter l’extension, la maintenance et la personnalisation des langues et dialectes

---

## 📁 Structure recommandée

- `ar/translation.json` : Traductions en arabe standard
- `ber/translation.json` : Traductions en berbère (amazigh)
- `fr/translation.json` : Traductions en français
- `en/translation.json` : Traductions en anglais
- `dialectes.json` : Métadonnées et descriptions des dialectes supportés (dz, ma, tn, kab, chaoui, mzab, rif, souss…)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Pas de données personnelles dans les fichiers de traduction, conformité RGPD, auditabilité des modifications.
- **SEO** : Mots-clés et descriptions optimisés pour chaque langue/dialecte.
- **Extensibilité** : Ajout facile de nouvelles langues ou dialectes.
- **Accessibilité** : Traductions adaptées pour tous les publics, prise en charge des langues régionales.
- **Documentation** : Structure claire, exemples d’utilisation, conventions de nommage.

---

## 📝 Exemple d’utilisation

```js
import i18n from 'i18next';
import ar from './ar/translation.json';
import fr from './fr/translation.json';
import en from './en/translation.json';
import ber from './ber/translation.json';

i18n.init({
  resources: {
    ar: { translation: ar },
    fr: { translation: fr },
    en: { translation: en },
    ber: { translation: ber }
  },
  lng: 'fr',
  fallbackLng: 'en'
});
```

---

## 📚 Documentation associée

- [dialectes.json](./dialectes.json)
- [Utils](../../utils/README.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : internationalisation moderne, inclusive, sécurisée, robuste, extensible et conforme RGPD pour chaque génération.**