// Tests unitaires & intégration – Social
import { SocialController } from './social_controller.js';
describe('SocialController', () => {
  it('createPost – doit créer un post', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await SocialController.createPost(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
