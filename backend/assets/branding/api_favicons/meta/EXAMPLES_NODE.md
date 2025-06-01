# Dihya API Favicon – Exemples Node.js/Express

```js
const express = require('express');
const meta = require('./meta_favicon-api.json');
const app = express();

app.get('/api/meta/favicon', (req, res) => {
  res.json(meta);
});

app.listen(4004, () => console.log('Serveur meta favicon Dihya sur 4004'));
```
