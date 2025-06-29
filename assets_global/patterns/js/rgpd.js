// rgpd.js – RGPD, anonymisation, suppression/export
module.exports = {
  anonymize: (data) => `anonymized(${JSON.stringify(data)})`,
  exportData: (user) => `exported data for ${user}`,
};
