# Dihya API Favicons PNG – Exemples Fallback/Legacy

## Utilisation fallback PNG pour legacy
```html
<link rel="icon" type="image/png" href="/assets/branding/api_favicons/png/favicon-api.png" />
```

## Fallback Node.js
```js
app.get('/api/assets/branding/api_favicons/png/:file', (req, res) => {
  const file = req.params.file;
  if (fs.existsSync(file)) {
    res.sendFile(file);
  } else {
    res.status(404).json({ error: 'Favicon not found' });
  }
});
```
