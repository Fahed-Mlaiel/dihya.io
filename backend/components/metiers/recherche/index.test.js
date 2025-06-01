// Tests unitaires & intégration – Recherche
import { RechercheController } from './recherche_controller.js';
describe('RechercheController', () => {
  it('search – doit retourner des résultats', async () => {
    const req = { query: { q: 'test' }, user: { role: 'user' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await RechercheController.search(req, res);
    expect(res.status).toHaveBeenCalledWith(200);
    expect(res.json).toHaveBeenCalledWith({ results: [] });
  });
});
