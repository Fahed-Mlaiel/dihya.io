// rgpd_checklist.js – Checklist RGPD

function getRGPDChecklist() {
  return [
    'Données chiffrées au repos',
    'Accès restreint par rôles',
    'Audit trail activé',
    'Politique de rétention documentée',
    'Procédures d’anonymisation en place',
    'Droit à l’oubli opérationnel',
    'Documentation utilisateur RGPD'
  ];
}

module.exports = { getRGPDChecklist };
