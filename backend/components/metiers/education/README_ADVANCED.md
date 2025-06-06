# Documentation avancée Education

## Intégration
- Ajoutez les routes du module à votre application FastAPI :
```python
from backend.components.metiers.education.views import router as education_router
app.include_router(education_router, prefix="/education")
```

## Extension
- Ajoutez vos propres plugins via `plugins.py`.
- Personnalisez les schémas dans `schemas.py`.
- Ajoutez des templates personnalisés dans `templates/`.

## Sécurité & RGPD
- Voir les guides dans `guides/` pour la conformité RGPD, la sécurité et l'accessibilité.

## Tests
- Lancez les tests avec `pytest` ou `npm test` selon le langage.

## Legacy
- Le dossier `legacy/` contient les API et tests pour la compatibilité ascendante.
