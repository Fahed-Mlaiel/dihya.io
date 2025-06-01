# Plugins IA pour Dihya

Ce dossier contient des plugins IA souverains (LLaMA, Mixtral, Mistral, etc.) pour l'intégration avancée dans les projets d'intelligence artificielle.

## Ajouter un plugin
- Placez votre plugin Python ici (ex: `llama_plugin.py`).
- Respectez l'interface : chaque plugin doit exposer une classe `IAPlugin` avec une méthode `generate(text, **kwargs)`.
- Les plugins sont chargés dynamiquement via l'API ou le CLI.

## Exemple minimal
```python
class IAPlugin:
    def generate(self, text, **kwargs):
        return f"Réponse IA pour: {text}"
```

## Sécurité
- Plugins isolés (sandbox), audités, logs RGPD.
- Chargement désactivé par défaut en production (voir doc sécurité).

## Multilingue
- Les plugins doivent supporter l'i18n (fr, en, ar, ...).

## Tests
- Ajoutez un fichier `test_<plugin>.py` pour chaque plugin.
