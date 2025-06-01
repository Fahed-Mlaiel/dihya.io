# Dihya API Favicon – Exemples Fallback/Legacy

## Utilisation fallback JSON pour legacy
```js
app.get('/api/meta/favicon', (req, res) => {
  try {
    res.json(require('./meta_favicon-api.json'));
  } catch {
    res.status(404).json({ error: 'Meta favicon not found' });
  }
});
```
