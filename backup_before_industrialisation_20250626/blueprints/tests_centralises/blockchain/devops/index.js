globalThis.tests = globalThis.tests || {};
const { runPipeline, getPipelineStatus } = require('../../../../blockchain/devops/pipeline');
describe('DevOps Pipeline', () => {
  it('exécute un pipeline CI/CD complet', async () => {
    const result = await runPipeline('deploy');
    expect(result.success).toBe(true);
  });
  it('récupère le statut du pipeline', () => {
    const status = getPipelineStatus('deploy');
    expect(['success', 'failed', 'running']).toContain(status);
  });
});
