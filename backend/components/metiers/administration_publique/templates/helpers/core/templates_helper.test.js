// templates_helper.test.js – Tests unitaires JS pour helpers templates Threed
const helper = require('./templates_helper');
describe('Helpers templates Threed (JS)', () => {
  test('renderTemplate fonctionne', () => {
    expect(typeof helper.renderTemplate).toBe('function');
  });
  test('isValidTemplate fonctionne', () => {
    expect(helper.isValidTemplate('rapport_audit.html.j2')).toBeTruthy();
    expect(helper.isValidTemplate('foo.txt')).toBeTruthy();
    expect(helper.isValidTemplate('foo.exe')).toBeFalsy();
  });
  test('mockTemplateContext retourne un objet', () => {
    expect(typeof helper.mockTemplateContext()).toBe('object');
  });
});

const TemplatesHelper = require('./templates_helper');

describe('TemplatesHelper', () => {
  it('doit s\'initialiser correctement', () => {
    const helper = new TemplatesHelper({ mode: 'test' });
    expect(helper.options).toEqual({ mode: 'test' });
    expect(helper.getAuditTrail()).toEqual([]);
  });

  it('doit initialiser la config et auditer', () => {
    const helper = new TemplatesHelper();
    expect(helper.init({ version: 1 })).toBe(true);
    expect(helper.config).toEqual({ version: 1 });
    expect(helper.getAuditTrail()[0].action).toBe('init');
  });

  it('doit assister une opération valide et auditer', () => {
    const helper = new TemplatesHelper();
    helper.init({ version: 2 });
    const result = helper.assist('OP', { foo: 'bar' });
    expect(result).toEqual({ success: true, operation: 'OP', data: { foo: 'bar' }, config: { version: 2 } });
    expect(helper.getAuditTrail().length).toBe(2);
    expect(helper.getAuditTrail()[1].action).toBe('assist');
  });

  it('doit lever une erreur sur une opération invalide et auditer', () => {
    const helper = new TemplatesHelper();
    expect(() => helper.assist(null, {})).toThrow('Invalid operation');
    expect(helper.getAuditTrail()[0].action).toBe('error');
  });
});
