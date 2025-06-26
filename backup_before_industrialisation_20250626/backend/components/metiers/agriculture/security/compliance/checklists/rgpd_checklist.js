// rgpd_checklist.js – Checklist RGPD

function getRGPDChecklist() {
  return [
    'Données chiffrées au repos',
    'Accès restreint par rôles',
    'Audit trail activé',
    'Politique de rétention documentée',
    "Procedures d'anonymisation en place",
    "Droit a l'oubli operationnel",
    'Documentation utilisateur RGPD'
  ];
}

module.exports = { getRGPDChecklist };
