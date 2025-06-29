// tests_grafana.js - Tests ultra avancés pour l'intégration Grafana

const { getGrafanaDashboards } = require('../../../../../../api/monitoring/grafana.js');

test('Dashboard Grafana présent', () => {
  const dashboards = getGrafanaDashboards();
  expect(Array.isArray(dashboards)).toBe(true);
  expect(dashboards.length).toBeGreaterThan(0);
});

// Convention : chaque intégration monitoring doit être testée sur au moins un scénario métier réel.
