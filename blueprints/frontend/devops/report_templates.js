// Script de reporting simple sur les templates (nombre, props, docs)
const fs = require('fs');
const path = require('path');

const TEMPLATES_DIR = path.join(__dirname, '../src/components/templates');

function reportTemplates() {
  const files = fs.readdirSync(TEMPLATES_DIR).filter(f => f.endsWith('.jsx'));
  const report = files.map(file => {
    const name = file.replace('.jsx', '');
    const content = fs.readFileSync(path.join(TEMPLATES_DIR, file), 'utf8');
    return {
      component: name,
      lines: content.split('\n').length,
      hasReadme: fs.existsSync(path.join(TEMPLATES_DIR, `README.md`)),
      hasExample: fs.existsSync(path.join(TEMPLATES_DIR, `README_EXEMPLES.md`))
    };
  });
  fs.writeFileSync(
    path.join(__dirname, 'report_templates.json'),
    JSON.stringify(report, null, 2)
  );
  console.log('Reporting terminé. Voir report_templates.json');
}

reportTemplates();
