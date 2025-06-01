# Politique Métier Automobile

## Accès et rôles
- **Admin** : gestion complète (CRUD véhicules, diagnostics, utilisateurs, plugins).
- **User** : accès lecture/écriture sur ses véhicules, diagnostics, support IA.
- **Invité** : accès lecture publique, pas de modification.

## Sécurité
- Authentification JWT obligatoire.
- CORS strict, WAF, anti-DDOS, audit logging.
- RGPD : anonymisation, export, suppression sur demande.

## Conformité
- Respect des normes ISO 26262, RGPD, accessibilité numérique.

## Plugins
- Ajout de modules via API/CLI sécurisé.

## Internationalisation
- Support multilingue dynamique (fr, en, ar, de, etc.).
