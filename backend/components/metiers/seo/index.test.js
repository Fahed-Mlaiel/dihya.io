// Tests unitaires & intégration – SEO
import { SEOController } from './seo_controller.js';
describe('SEOController', () => {
  it('createSeoEntry – doit créer une entrée SEO', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await SEOController.createSeoEntry(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
