// Script de reporting simple sur les organisms (nombre, props, docs)
const fs = require('fs');
const path = require('path');

const ORGANISMS_DIR = path.join(__dirname, '../src/components/organisms');

function reportOrganisms() {
  const files = fs.readdirSync(ORGANISMS_DIR).filter(f => f.endsWith('.jsx'));
  const report = files.map(file => {
    const name = file.replace('.jsx', '');
    const content = fs.readFileSync(path.join(ORGANISMS_DIR, file), 'utf8');
    return {
      component: name,
      lines: content.split('\n').length,
      hasReadme: fs.existsSync(path.join(ORGANISMS_DIR, `README.md`)),
      hasExample: fs.existsSync(path.join(ORGANISMS_DIR, `README_EXEMPLES.md`))
    };
  });
  fs.writeFileSync(
    path.join(__dirname, 'report_organisms.json'),
    JSON.stringify(report, null, 2)
  );
  console.log('Reporting terminé. Voir report_organisms.json');
}

reportOrganisms();
