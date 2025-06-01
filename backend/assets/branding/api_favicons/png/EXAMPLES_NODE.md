# Dihya API Favicons PNG – Exemples Node.js/Express

```js
const express = require('express');
const path = require('path');
const app = express();

app.get('/api/assets/branding/api_favicons/png/:file', (req, res) => {
  const file = req.params.file;
  res.sendFile(path.join(__dirname, file));
});

app.listen(4003, () => console.log('Serveur favicons PNG Dihya sur 4003'));
```
