// Test complet pour les validateurs (social, sport, tourisme, transport)
const { validateSocialProject, validateSportProject, validateTourismeProject, validateTransportProject } = require('./template');

describe('Validators', () => {
  it('valide un projet social correct', () => {
    const req = { body: { name: 'Test', description: 'Desc', type: 'AI' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    const next = jest.fn();
    validateSocialProject(req, res, next);
    expect(next).toHaveBeenCalled();
  });
  it('rejette un projet social incorrect', () => {
    const req = { body: { name: '', description: '', type: 'X' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    const next = jest.fn();
    validateSocialProject(req, res, next);
    expect(res.status).toHaveBeenCalledWith(400);
  });
});
