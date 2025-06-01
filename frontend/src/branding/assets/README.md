# 🏷️ Branding Assets – Dihya Coding

Ce dossier contient tous les assets de branding (logos, couleurs, polices, chartes graphiques, templates) utilisés pour l’identité visuelle de Dihya Coding.  
L’organisation et la gestion de ces ressources respectent : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité et robustesse.

---

## 🎨 Bonnes pratiques

- **Design** : Respect de la charte graphique Dihya, cohérence visuelle, haute résolution, adaptabilité dark/light mode.
- **SEO** : Noms de fichiers explicites, attributs `alt` pour les images, formats modernes (SVG, WebP).
- **Performance** : Compression optimisée, formats vectoriels privilégiés, lazy loading pour les médias lourds.
- **Accessibilité** : Texte alternatif descriptif, titres ou `aria-label` pour chaque asset visuel.
- **RGPD** : Aucun asset ne doit contenir de données personnelles ou sensibles (vérification des métadonnées).
- **Auditabilité** : Historique des ajouts/modifications via Git, documentation de la provenance et des droits d’utilisation.
- **Extensibilité** : Ajout facile de nouveaux assets en respectant la structure et la nomenclature.

---

## 📁 Structure recommandée

- `logos/` : Logos principaux et variantes (SVG, PNG)
- `colors/` : Palettes de couleurs officielles (fichiers JSON, CSS, SCSS)
- `fonts/` : Polices personnalisées ou libres de droits
- `templates/` : Templates de branding (présentations, mockups, etc.)
- `guidelines/` : Chartes graphiques et guides d’utilisation

---

## 🛡️ Sécurité & conformité

- Utiliser uniquement des ressources libres de droits ou créées pour Dihya Coding.
- Nettoyer les métadonnées (EXIF, GPS, etc.) avant ajout.
- Respecter la charte graphique et la politique de branding.
- Documentation claire sur la provenance et les droits d’utilisation de chaque asset.

---

## 📝 Exemple d’utilisation

```jsx
import logoDihya from './logos/dihya-logo.svg';

function AppHeader() {
  return <img src={logoDihya} alt="Logo Dihya Coding" aria-label="Logo Dihya Coding" />;
}
```

---

> **Dihya Coding : une identité visuelle moderne, souveraine et conforme.**