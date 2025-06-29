// security_policy_fr.js – Politique de sécurité (exemple)

function getSecurityPolicy() {
  return `Politique d’audit :\n- Audit automatisé hebdomadaire\n- Revue manuelle mensuelle\n- Conservation des logs 12 mois minimum\n- Alertes automatiques en cas d’anomalie`;
}

module.exports = { getSecurityPolicy };
