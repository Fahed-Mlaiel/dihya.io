// Test unitaire pour sample_template_model.js
describe('Template Model', () => {
  it('should return a valid template model', () => {
    const { getTemplateModel } = require('./sample_template_model');
    const model = getTemplateModel();
    expect(model.valid).toBe(true);
    expect(model.fields).toContain('id');
    expect(model.type).toBe('model');
  });
});
