# Tests API Centralisés

Tests ultra avancés pour la validation des blueprints API (routes, contrôleurs, sécurité, etc.) en JS et Python.

## Fonctionnalités incluses
- Tests unitaires et d’intégration pour chaque endpoint
- Mocking, fixtures, validation des réponses et erreurs
- Exemples d'intégration Node.js et Python

## Exemples d'intégration

### Node.js
```js
describe('GET /api/assets', () => {
  it('doit retourner la liste des assets', async () => {
    const res = await request(app).get('/api/assets');
    expect(res.status).toBe(200);
    expect(res.body.assets).toBeDefined();
  });
});
```

### Python
```python
def test_get_assets(client):
    response = client.get('/api/assets')
    assert response.status_code == 200
    assert 'assets' in response.json
```

## Bonnes pratiques
- Ajoutez des tests pour chaque route et cas d’erreur
- Utilisez des fixtures pour simuler les données métiers

