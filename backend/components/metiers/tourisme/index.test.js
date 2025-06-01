// Tests unitaires & intégration – Tourisme
import { TourismeController } from './tourisme_controller.js';
describe('TourismeController', () => {
  it('createAttraction – doit créer une attraction', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await TourismeController.createAttraction(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
