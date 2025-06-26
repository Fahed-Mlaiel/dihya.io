// Script de reporting simple sur les atoms (nombre, props, docs)
const fs = require('fs');
const path = require('path');

const ATOMS_DIR = path.join(__dirname, '../src/components/atoms');

function reportAtoms() {
  const files = fs.readdirSync(ATOMS_DIR).filter(f => f.endsWith('.jsx'));
  const report = files.map(file => {
    const name = file.replace('.jsx', '');
    const content = fs.readFileSync(path.join(ATOMS_DIR, file), 'utf8');
    return {
      component: name,
      lines: content.split('\n').length,
      hasReadme: fs.existsSync(path.join(ATOMS_DIR, `README.md`)),
      hasExample: fs.existsSync(path.join(ATOMS_DIR, `README_EXEMPLES.md`))
    };
  });
  fs.writeFileSync(
    path.join(__dirname, 'report_atoms.json'),
    JSON.stringify(report, null, 2)
  );
  console.log('Reporting terminé. Voir report_atoms.json');
}

reportAtoms();
