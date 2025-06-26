// Test ultra avancé du middleware threedInput (Node.js)
const threedInput = require('../../../middlewares/validation/input/threed_input');

describe('threedInput middleware', () => {
  it('laisse passer si req.body existe', () => {
    const req = { body: { foo: 'bar' } };
    const res = {};
    const next = jest.fn();
    threedInput(req, res, next);
    expect(next).toHaveBeenCalled();
  });

  it('retourne 400 si req.body est manquant', () => {
    const req = {};
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    const next = jest.fn();
    threedInput(req, res, next);
    expect(res.status).toHaveBeenCalledWith(400);
    expect(res.json).toHaveBeenCalledWith({ error: 'Aucune donnée fournie' });
    expect(next).not.toHaveBeenCalled();
  });
});
