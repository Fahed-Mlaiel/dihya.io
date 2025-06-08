describe('templates core', () => {
  it('should render a threed template', () => {
    const { renderThreedTemplate } = require('./template_threed.js');
    expect(renderThreedTemplate({ title: 'Test' })).toContain('Test');
  });
});
