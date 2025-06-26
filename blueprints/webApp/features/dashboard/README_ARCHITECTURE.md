# Architecture – Dashboard

## Schéma d’architecture (ASCII)
```
[DashboardHome] [AnalyticsPanel] [DashboardStats] [DashboardSettings] [NotificationPanel]
      |                |                |                |
   [useAuth]      [useAnalytics]   [apiService]   [useNotification]
```

- **DashboardHome** : Accueil du dashboard utilisateur
- **AnalyticsPanel** : Panneau analytics
- **DashboardStats** : Statistiques avancées
- **DashboardSettings** : Paramètres utilisateur
- **NotificationPanel** : Notifications en temps réel
