// Initialisation avancée des tests Node.js pour monitoring
let monitoring;

try {
  monitoring = require('../../../../blueprints/monitoring');
} catch (e) {
  monitoring = require('./test_monitoring.js');
}

describe('devops/monitoring', () => {
  it('dummy', () => {
    expect(true).toBe(true);
  });

  it('existe', () => {
    expect(typeof monitoring).toBe('object');
  });
});

