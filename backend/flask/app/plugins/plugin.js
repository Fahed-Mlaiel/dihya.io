// plugin.js - Exemple de plugin Dihya (Node.js)
// Plugin extensible, sécurisé, internationalisé, documenté
module.exports = {
  name: 'exemplePlugin',
  description: {
    fr: 'Plugin exemple pour Dihya',
    en: 'Example plugin for Dihya',
    ar: 'إضافة مثال لـ Dihya',
    de: 'Beispiel-Plugin für Dihya',
    zh: 'Dihya 示例插件',
    ja: 'Dihya用サンプルプラグイン',
    ko: 'Dihya 예제 플러그인',
    nl: 'Voorbeeldplugin voor Dihya',
    he: 'תוסף לדוגמה עבור Dihya',
    fa: 'افزونه نمونه برای Dihya',
    hi: 'Dihya के लिए उदाहरण प्लगइन',
    es: 'Plugin de ejemplo para Dihya'
  },
  version: '1.0.0',
  init: (app, options) => {
    // ...initialisation plugin...
    app.use('/api/plugins/exemple', (req, res) => {
      res.json({ message: 'Plugin exemple actif', lang: req.headers['accept-language'] || 'fr' });
    });
  }
};
