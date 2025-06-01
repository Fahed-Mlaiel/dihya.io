# Dihya API Favicon – Exemples RBAC (Rôles & Permissions)

## Node.js/Express
```js
app.use((req, res, next) => {
  const role = req.headers['x-role'] || 'invite';
  if (role !== 'admin' && req.path.includes('favicon')) {
    return res.status(403).json({ error: 'Accès refusé' });
  }
  next();
});
```

## Django
```python
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def favicon_meta_view(request):
    ...
```
