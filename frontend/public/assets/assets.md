# 🗂️ Dihya – Frontend Public Assets Guide

Ce dossier contient tous les assets publics du frontend Dihya : images, icônes, logos, polices, vidéos, sons, templates, etc.

---

## Structure recommandée

- **/images/** : illustrations, backgrounds, UI
- **/icons/** : icônes SVG/React accessibles, multilingues
- **/logos/** : logos Dihya (clair, sombre, amazigh, métiers)
- **/fonts/** : polices open source, multilingues (fr, en, ar, tzr)
- **/videos/** : démos, tutoriels, branding
- **/audio/** : sons UI, notifications, branding
- **/templates/** : wireframes, snippets, modèles UI

---

## Multilingue & Accessibilité

- Tous les assets critiques sont fournis en versions multilingues (fr, en, ar, tzr) et testés pour l’accessibilité (contraste, aria-label, alt, focusable).
- Les polices couvrent tous les alphabets nécessaires (latin, arabe, tifinagh…).
- Les images et vidéos sont optimisées pour le web (WebP, SVG, compression lossless).

---

## Bonnes pratiques

- Utilisez des assets open source, sans tracking, souverains.
- Ajoutez un alt/aria-label pertinent pour chaque image/icône.
- Vérifiez la performance (taille, format) et la conformité RGPD.

---

## Contribution

1. Placez votre asset dans le dossier approprié.
2. Ajoutez-le dans le registre (`index.js` ou équivalent) si besoin.
3. Vérifiez : accessibilité, performance, souveraineté, documentation.

---

## Exemples d’intégration

- **React** : import direct via `import img from './images/mon_image.webp'`
- **HTML** : `<img src="/assets/images/mon_image.webp" alt="..." />`

---

## Contact & support
Pour toute question : [support@dihya.io](mailto:support@dihya.io)
