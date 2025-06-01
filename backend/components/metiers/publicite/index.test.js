// Tests unitaires & intégration – Publicité
import { PubliciteController } from './publicite_controller.js';
describe('PubliciteController', () => {
  it('createCampaign – doit créer une campagne', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await PubliciteController.createCampaign(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
