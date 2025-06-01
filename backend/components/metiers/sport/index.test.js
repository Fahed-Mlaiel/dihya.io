// Tests unitaires & intégration – Sport
import { SportController } from './sport_controller.js';
describe('SportController', () => {
  it('createEvent – doit créer un événement', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await SportController.createEvent(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
