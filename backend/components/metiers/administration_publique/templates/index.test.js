// index.test.js – Test d’intégration du point d’entrée JS pour templates Threed
const entry = require('./index.js');

describe('Entrée JS templates Threed', () => {
  it('expose les helpers principaux', () => {
    expect(entry.renderTemplate).toBeDefined();
    expect(entry.isValidTemplate).toBeDefined();
    expect(entry.mockTemplateContext).toBeDefined();
  });
  it('expose les validateurs principaux', () => {
    expect(entry.isValidTemplateFile).toBeDefined();
    expect(entry.validateTemplateContent).toBeDefined();
  });
});
