# 🧪 Tests – Branding Dihya Coding

Ce dossier contient les tests unitaires et d’intégration pour le module de branding (identité visuelle) de Dihya Coding.  
Les tests garantissent : robustesse, conformité RGPD, auditabilité, sécurité, extensibilité et documentation claire.

---

## 🎯 Objectifs des tests

- **Vérifier la conformité des assets de branding (logos, couleurs, polices, templates)**
- **Assurer l’absence de données personnelles ou sensibles dans les fichiers**
- **Garantir la cohérence graphique et l’accessibilité (attributs alt, aria-label, contrastes)**
- **Documenter les cas d’usage métier et les scénarios critiques**
- **Vérifier la bonne organisation et la nomenclature des fichiers**

---

## 🛡️ Bonnes pratiques

- **Isolation** : Chaque test doit être indépendant et réinitialiser l’état local (mocks, fichiers temporaires).
- **Sécurité** : Vérifier l’absence de métadonnées sensibles (EXIF, GPS) dans les assets.
- **Auditabilité** : Historique des modifications via Git, logs de tests.
- **Extensibilité** : Ajouter facilement de nouveaux tests pour chaque nouvel asset ou règle de branding.
- **Documentation** : Utiliser des descriptions claires et des docstrings pour chaque scénario.

---

## 📝 Structure recommandée

- `branding.spec.js` : Tests unitaires des assets et règles de branding
- `branding.integration.spec.js` : Tests d’intégration (chargement, accessibilité, cohérence)
- `__mocks__/` : Mocks pour fichiers, images, polices, etc.

---

## 🧩 Exemple de test (Jest)

```js
import logo from '../assets/logos/dihya-logo.svg';

describe('Branding Assets', () => {
  it('doit avoir un nom de fichier explicite', () => {
    expect(logo).toMatch(/dihya-logo\.svg$/);
  });

  it('doit être accessible (alt et aria-label)', () => {
    // Exemple de test React
    const img = <img src={logo} alt="Logo Dihya Coding" aria-label="Logo Dihya Coding" />;
    expect(img.props.alt).toBeTruthy();
    expect(img.props['aria-label']).toBeTruthy();
  });
});
```

---

## 📚 Documentation associée

- [Branding assets](../assets/README.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : des tests pour une identité visuelle moderne, souveraine et conforme.**