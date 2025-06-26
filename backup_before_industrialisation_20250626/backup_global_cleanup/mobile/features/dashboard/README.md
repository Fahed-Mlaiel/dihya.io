# Dashboard – Feature métier

Ce dossier gère le tableau de bord utilisateur (statistiques, notifications, paramètres, etc.).

## Composants
- DashboardHome.jsx
- DashboardStats.jsx
- DashboardSettings.jsx
- AnalyticsPanel.jsx
- NotificationPanel.jsx

## Cas d’usage
- Affichage des statistiques personnalisées
- Gestion des notifications en temps réel
- Accès rapide aux paramètres utilisateur

## Flux utilisateur
1. L’utilisateur accède au dashboard après login
2. Visualise ses stats, notifications, paramètres

## Exemples d’intégration
```jsx
import DashboardHome from './DashboardHome';
<DashboardHome user={user} />
```

## Schéma d’architecture
[DashboardHome] → [AnalyticsPanel] → [useAnalytics]
[DashboardHome] → [NotificationPanel] → [useNotification]
