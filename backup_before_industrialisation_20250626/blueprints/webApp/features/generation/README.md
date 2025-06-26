# Generation – Feature métier

Ce dossier gère la génération de projets, templates, et l’historique des générations.

## Composants
- Generator.jsx
- GenerationHistory.jsx
- TemplateSelector.jsx

## Cas d’usage
- Génération de projet No-Code/Low-Code
- Sélection de template métier
- Historique des générations

## Flux utilisateur
1. L’utilisateur sélectionne un template
2. Génère un projet
3. Consulte l’historique

## Exemples d’intégration
```jsx
import Generator from './Generator';
<Generator templateId={1} />
```

## Schéma d’architecture
[Generator] → [TemplateSelector] → [GenerationHistory]
