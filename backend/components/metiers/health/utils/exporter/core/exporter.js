// exporter.js – Export CSV/JSON, anonymisation, RGPD, audit pour Health (health)
const fs = require('fs');

module.exports = {
  exportToJSON: (data, filepath) => {
    fs.writeFileSync(filepath, JSON.stringify(data, null, 2), 'utf-8');
    return filepath;
  },
  exportToCSV: (data, filepath) => {
    if (!Array.isArray(data) || data.length === 0) return filepath;
    const keys = Object.keys(data[0]);
    const csv = [keys.join(',')].concat(data.map(row => keys.map(k => row[k]).join(','))).join('\n');
    fs.writeFileSync(filepath, csv, 'utf-8');
    return filepath;
  },
  anonymize: (data) => {
    // Simule l'anonymisation RGPD
    return Array.isArray(data)
      ? data.map(row => ({ ...row, user: 'anonyme' }))
      : { ...data, user: 'anonyme' };
  }
};
