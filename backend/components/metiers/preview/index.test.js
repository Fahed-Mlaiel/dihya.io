// Tests unitaires & intégration – Preview
import { PreviewController } from './preview_controller.js';
describe('PreviewController', () => {
  it('createPreview – doit créer un preview', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await PreviewController.createPreview(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
