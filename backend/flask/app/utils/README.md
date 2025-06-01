# utils/ — Utilitaires Backend Flask Dihya Coding

Ce dossier contient tous les modules utilitaires réutilisables pour le backend Flask Dihya Coding.

## Contenu

- **i18n.py** : Fonctions d'internationalisation, détection de langue, traduction locale et dynamique à la volée (API).
- **i18n_dynamic.py** : Traduction multilingue automatique via API open source ([LibreTranslate](https://libretranslate.com/)), support de toutes les langues/dialectes sans fichiers manuels.
- **i18n_dynamic_config.py** : Configuration centralisée de l’API de traduction dynamique (URL, langue par défaut, timeout…).
- **mailing.py** : Fonctions d'envoi d’e-mails (abstraction de Flask-Mail, validation, sécurité).
- **security.py** : Fonctions de sécurité (hash, vérification de mot de passe, génération de tokens, validation JWT, etc.).
- **seo.py** : Fonctions utilitaires pour le SEO (robots.txt, sitemap.xml, balises, perf Lighthouse, etc.).
- **validators.py** : Fonctions de validation personnalisées pour les schémas ou les entrées API.
- **rate_limit.py** : Décorateur de limitation de débit et anti-DDoS.
- **error_handling.py** : Gestion centralisée des erreurs et réponses API.
- **cors.py** : Configuration avancée du CORS (origines autorisées, sécurité).
- **exceptions.py** : Exceptions personnalisées pour la gestion métier et la sécurité.

## Bonnes pratiques

- Chaque utilitaire doit être documenté avec une docstring claire et un exemple d’utilisation si pertinent.
- Les fonctions doivent être génériques et réutilisables dans plusieurs modules.
- Ne pas inclure de logique métier spécifique ici : uniquement des helpers/utilitaires.
- Préférer des fonctions pures, sans effet de bord.
- Ajouter des tests unitaires pour chaque fonction critique.
- Ne jamais inclure de secrets ou de données sensibles dans les logs ou les erreurs.
- Respecter la souveraineté numérique et la sécurité dans chaque helper.
- Pour l’i18n dynamique, privilégier une API open source hébergée pour la souveraineté et prévoir un fallback local.

## Exemple d'utilisation

```python
from app.utils.security import hash_password, verify_password

hashed = hash_password("monmotdepasse")
assert verify_password("monmotdepasse", hashed)

from app.utils.rate_limit import rate_limit

@app.route("/api/secure")
@rate_limit(limit=10, window=60)
def secure_endpoint():
    return "OK"

from app.utils.cors import configure_cors
configure_cors(app)

from app.utils.i18n import translate
msg = translate("Bienvenue sur Dihya Coding !", lang="ar")

from app.utils.i18n_dynamic import translate_dynamic
msg_auto = translate_dynamic("Bienvenue sur Dihya Coding !", "en")