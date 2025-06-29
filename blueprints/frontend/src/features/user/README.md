# User – Feature métier

Ce dossier gère la gestion utilisateur (profil, paramètres, audit, RGPD, etc.).

## Composants
- UserProfile.jsx
- UserSettings.jsx
- UserAvatar.jsx
- AuditPanel.jsx
- RGPDPanel.jsx

## Cas d’usage
- Affichage et édition du profil utilisateur
- Gestion des paramètres et préférences
- Audit des accès et conformité RGPD

## Flux utilisateur
1. L’utilisateur accède à son profil
2. Modifie ses infos ou préférences
3. Consulte l’audit ou RGPDPanel

## Exemples d’intégration
```jsx
import UserProfile from './UserProfile';
<UserProfile user={user} />
```

## Schéma d’architecture
[UserProfile] → [UserSettings] → [AuditPanel] → [RGPDPanel]
