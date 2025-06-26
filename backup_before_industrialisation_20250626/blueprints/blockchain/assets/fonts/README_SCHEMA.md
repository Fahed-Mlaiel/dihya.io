# Schéma d’architecture – Polices

- OpenSans-Regular.woff : Police principale
- Roboto-Regular.woff : Police secondaire
- font-OpenSans-v2.woff : Version optimisée, multilingue

Organisation :
```
fonts/
  OpenSans-Regular.woff
  Roboto-Regular.woff
  font-OpenSans-v2.woff
  index.js
  ...
```

## Mapping métier (fonts.mapping.json)
- OpenSans-Regular.woff : général, interface, accessibilité, multilingue
- Roboto-Regular.woff : moderne, mobile, accessibilité
- font-OpenSans-v2.woff : multilingue, alphabets étendus
- NotoSansArabic.woff : arabe, branding international
- Tifinagh.woff : amazigh, branding local

## Convention de nommage
- font-NOM[-vX].woff
- Toujours versionner en cas de modification majeure
