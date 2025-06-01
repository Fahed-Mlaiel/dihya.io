// Tests unitaires & intégration – Transport
import { TransportController } from './transport_controller.js';
describe('TransportController', () => {
  it('createRoute – doit créer une route', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await TransportController.createRoute(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
