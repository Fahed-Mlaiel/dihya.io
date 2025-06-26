// Test ultra avancé du middleware threedSchema (Node.js)
const threedSchema = require('../../../middlewares/validation/schema/threed_schema');

describe('threedSchema middleware', () => {
  it('appelle validate si req.schema existe', () => {
    const validate = jest.fn();
    const req = { schema: { validate }, body: { foo: 'bar' } };
    const res = {};
    const next = jest.fn();
    threedSchema(req, res, next);
    expect(validate).toHaveBeenCalledWith({ foo: 'bar' });
    expect(next).toHaveBeenCalled();
  });

  it('n’appelle pas validate si req.schema absent', () => {
    const req = { body: { foo: 'bar' } };
    const res = {};
    const next = jest.fn();
    threedSchema(req, res, next);
    expect(next).toHaveBeenCalled();
  });
});
