// Script de reporting simple sur les molecules (nombre, props, docs)
const fs = require('fs');
const path = require('path');

const MOLECULES_DIR = path.join(__dirname, '../src/components/molecules');

function reportMolecules() {
  const files = fs.readdirSync(MOLECULES_DIR).filter(f => f.endsWith('.jsx'));
  const report = files.map(file => {
    const name = file.replace('.jsx', '');
    const content = fs.readFileSync(path.join(MOLECULES_DIR, file), 'utf8');
    return {
      component: name,
      lines: content.split('\n').length,
      hasReadme: fs.existsSync(path.join(MOLECULES_DIR, `README.md`)),
      hasExample: fs.existsSync(path.join(MOLECULES_DIR, `README_EXEMPLES.md`))
    };
  });
  fs.writeFileSync(
    path.join(__dirname, 'report_molecules.json'),
    JSON.stringify(report, null, 2)
  );
  console.log('Reporting terminé. Voir report_molecules.json');
}

reportMolecules();
