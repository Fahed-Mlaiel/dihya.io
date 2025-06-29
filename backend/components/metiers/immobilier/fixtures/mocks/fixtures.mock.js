/* global jest */
// fixtures.mock.js - Mocks pour tests unitaires et intégration Immobilier

module.exports = {
  mockRequest: (data = {}) => ({
    body: data,
    headers: { 'x-test': 'true' },
    user: { id: 'mock-user', role: 'test' }
  }),
  mockResponse: () => {
    const res = {};
    res.status = jest.fn().mockReturnValue(res);
    res.json = jest.fn().mockReturnValue(res);
    return res;
  }
};
