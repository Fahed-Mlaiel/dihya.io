# Schéma d’architecture du store

```ascii
+-------------------+
|    userStore      |
+-------------------+
| isAuthenticated   |
| user              |
| roles             |
| locale            |
+-------------------+
        |
        v
+-------------------+
|   Autres stores   |
+-------------------+
```

Chaque module/slice est indépendant et exporté via `index.js`.
