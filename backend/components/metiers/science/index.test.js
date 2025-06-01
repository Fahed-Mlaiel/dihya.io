// Tests unitaires & intégration – Science
import { ScienceController } from './science_controller.js';
describe('ScienceController', () => {
  it('createExperiment – doit créer une expérience', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await ScienceController.createExperiment(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
