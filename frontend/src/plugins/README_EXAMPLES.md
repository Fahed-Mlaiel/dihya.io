# Dihya Frontend – Plugins (exemple)

Ce dossier est prêt à accueillir des plugins dynamiques pour l’extension des fonctionnalités frontend Dihya (IA, VR, AR, etc.).

Exemple de plugin IA :

```js
// src/plugins/iaFallback.js
export function iaFallback(input) {
  // Fallback IA open source (ex: LLaMA, Mixtral, Mistral)
  return `Réponse IA pour: ${input}`;
}
```

Utilisation : voir README principal et src/plugins/README.md
