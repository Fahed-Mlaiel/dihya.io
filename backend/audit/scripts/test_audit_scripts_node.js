// Tests unitaires ultra avancés pour les scripts d’audit Node.js (main.js)
// Utilise Jest (ou équivalent) pour valider l’intégrité, la génération de rapports, la robustesse RGPD/auditabilité

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const SCRIPT_ROOT = __dirname;
const ASSETS_ROOT = path.resolve(__dirname, '../../assets');

const REPORTS = [
  'integrity_report.csv',
  'integrity_report.json',
];

describe('Audit Node.js (main.js)', () => {
  beforeAll(() => {
    // Nettoyage des anciens rapports
    REPORTS.forEach(f => {
      const p = path.join(ASSETS_ROOT, f);
      if (fs.existsSync(p)) fs.unlinkSync(p);
    });
    // Exécution du script Node.js (génère les rapports)
    execSync('node main.js --lang fr --csv --json', { cwd: SCRIPT_ROOT });
  });

  test.each(REPORTS)('Le rapport %s est généré', (report) => {
    const p = path.join(ASSETS_ROOT, report);
    expect(fs.existsSync(p)).toBe(true);
  });

  test('Le rapport JSON est une liste non vide', () => {
    const jsonPath = path.join(ASSETS_ROOT, 'integrity_report.json');
    const data = JSON.parse(fs.readFileSync(jsonPath, 'utf-8'));
    expect(Array.isArray(data)).toBe(true);
    expect(data.length).toBeGreaterThan(0);
  });

  test('Le rapport CSV a un header et des lignes', () => {
    const csvPath = path.join(ASSETS_ROOT, 'integrity_report.csv');
    const lines = fs.readFileSync(csvPath, 'utf-8').split('\n').filter(Boolean);
    expect(lines.length).toBeGreaterThan(1);
    expect(lines[0]).toMatch(/Fichier|File/);
  });

  test('Aucune donnée personnelle dans les rapports', () => {
    const jsonPath = path.join(ASSETS_ROOT, 'integrity_report.json');
    const content = fs.readFileSync(jsonPath, 'utf-8').toLowerCase();
    const forbidden = ['nom réel','adresse','phone','téléphone','numéro','@gmail.com','@yahoo.com','dupont','durand','smith'];
    forbidden.forEach(word => {
      expect(content.includes(word)).toBe(false);
    });
  });
});
