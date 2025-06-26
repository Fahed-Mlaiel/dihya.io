// Tests avancés de monitoring pour la plateforme threed
describe('Monitoring', () => {
  it('doit vérifier la disponibilité de Prometheus', () => {
    const { execSync } = require('child_process');
    const output = execSync('curl -s http://localhost:9090/-/ready', { encoding: 'utf-8' });
    expect(output).toMatch(/Prometheus is Ready/);
  });
  it('doit vérifier la présence du dashboard Grafana', () => {
    const fs = require('fs');
    expect(fs.existsSync('/etc/grafana/provisioning/dashboards')).toBe(true);
  });
});
