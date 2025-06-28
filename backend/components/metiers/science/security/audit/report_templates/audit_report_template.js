// audit_report_template.js – Générateur de rapport d’audit

function generateAuditReport(date, auditor, findings) {
  return `Rapport d’audit – Sécurité science\nDate : ${date}\nAuditeur : ${auditor}\n\nRésumé :\n${findings}`;
}

module.exports = { generateAuditReport };
