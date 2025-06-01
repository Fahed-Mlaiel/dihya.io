# 🖼️ Images – Dihya Coding

Ce dossier contient les images utilisées dans l’interface de Dihya Coding.  
Les images sont sélectionnées et optimisées pour garantir : design moderne, accessibilité, performance, conformité RGPD et auditabilité.

---

## 🎨 Bonnes pratiques

- **Design** : Images cohérentes avec l’identité visuelle Dihya, haute qualité, responsive, adaptées au dark/light mode.
- **SEO** : Attributs `alt` descriptifs et pertinents pour chaque image, noms de fichiers explicites.
- **Performance** : Formats optimisés (WebP, SVG, PNG), compression sans perte, lazy loading recommandé.
- **Accessibilité** : Texte alternatif obligatoire, éviter les images porteuses d’information sans équivalent textuel.
- **RGPD** : Aucune donnée personnelle ou sensible dans les images ou leurs métadonnées.
- **Auditabilité** : Historique des ajouts/modifications via Git, documentation claire de la provenance des images.
- **Extensibilité** : Ajouter de nouvelles images en respectant la structure et la nomenclature.

---

## 📁 Structure recommandée

- `illustrations/` : Illustrations thématiques
- `backgrounds/` : Images de fond
- `logos/` : Logos et branding
- `screenshots/` : Captures d’écran de la plateforme

---

## 🛡️ Sécurité & conformité

- Utiliser uniquement des images libres de droits ou créées pour Dihya Coding.
- Vérifier et nettoyer les métadonnées avant ajout (ex : EXIF, GPS).
- Respecter la charte graphique et la politique de branding.

---

## 📝 Exemple d’utilisation (React)

```jsx
import heroImage from './illustrations/hero.webp';

function HeroSection() {
  return <img src={heroImage} alt="Présentation de Dihya Coding" loading="lazy" />;
}
```

---

> **Dihya Coding : des images modernes, accessibles et responsables.**