# Architecture – Features

## Schéma d’architecture (ASCII)
```
[auth] [dashboard] [docs] [generation] [marketplace] [plugins] [user]
   |        |         |         |           |           |
[LoginForm] [DashboardHome] [DocPage] [Generator] [MarketplaceList] [PluginManager] [UserProfile]
```

- **auth/** : Authentification (LoginForm, etc.)
- **dashboard/** : Dashboard utilisateur
- **docs/** : Documentation intégrée
- **generation/** : Génération de contenu
- **marketplace/** : Marketplace de templates/plugins
- **plugins/** : Gestion des plugins
- **user/** : Gestion du profil utilisateur
