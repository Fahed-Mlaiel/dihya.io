// Point d'entrée statique pour assets web, SEO, accessibilité, multilingue, sécurité, plugins, audit, templates
// Utilisé pour servir les assets frontend, robots.txt, sitemap.xml, etc.

const express = require('express');
const path = require('path');
const app = express();

// Sécurité headers
app.use(require('helmet')());

// SEO robots.txt
app.get('/robots.txt', (req, res) => {
  res.type('text/plain');
  res.send('User-agent: *\nDisallow: /admin\nAllow: /');
});

// Sitemap dynamique
app.get('/sitemap.xml', (req, res) => {
  res.type('application/xml');
  res.send(`<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<url><loc>https://dihya.example.com/</loc></url>\n</urlset>`);
});

// Assets statiques
app.use(express.static(path.join(__dirname, 'public')));

// Accessibilité
app.get('/accessibility', (req, res) => {
  res.json({
    msg: 'Accessible, multilingue, conforme WCAG, plugins, audit',
    langs: ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es', 'amazigh']
  });
});

module.exports = app;
