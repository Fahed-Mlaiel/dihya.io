# Dihya Frontend – SEO & Accessibilité (exemple)

Ce dossier est prêt à accueillir les fichiers SEO (robots.txt, sitemap.xml, manifest.json, favicon, etc.) et les guides d’accessibilité.

Exemple robots.txt :

```
User-agent: *
Disallow: /admin
```

Exemple sitemap.xml :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://dihya.example.com/</loc>
    <lastmod>2025-05-26</lastmod>
    <priority>1.0</priority>
  </url>
</urlset>
```

Utilisation : placer dans `public/` ou configurer via le framework.
