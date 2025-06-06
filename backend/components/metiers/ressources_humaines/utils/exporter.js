// exporter.js – Exportation avancée des données environnementales (Node.js)
const fs = require('fs');

module.exports = {
  exportToJSON: (data, filePath) => {
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
    return filePath;
  },
  exportToCSV: (data, filePath) => {
    const keys = Object.keys(data[0] || {});
    const csv = [keys.join(',')].concat(data.map(row => keys.map(k => row[k]).join(','))).join('\n');
    fs.writeFileSync(filePath, csv);
    return filePath;
  }
};
