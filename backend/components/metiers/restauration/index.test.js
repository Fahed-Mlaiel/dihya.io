// Tests unitaires & intégration – Restauration
import { RestaurationController } from './restauration_controller.js';
describe('RestaurationController', () => {
  it('createReservation – doit créer une réservation', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await RestaurationController.createReservation(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
