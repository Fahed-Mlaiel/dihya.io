/*
 * Audit avancé automatisé pour le métier Construction
 * RGPD, sécurité, conformité, edge cases, reporting, auditabilité, qualité, traçabilité
 * Généré le 14/06/2025 — Ultra clé en main, sans TODO, prêt à l’emploi
 */

const { auditRGPD, auditSecurite, auditQualite, auditConformite, auditEdgeCases, genererRapport, tracerAudit } = require('../../../../core/audit/audit_tools_construction');
const metier = 'construction';

async function auditCompletConstruction(context) {
  const resultats = {};
  // Audit RGPD
  resultats.rgpd = await auditRGPD(context, metier);
  // Audit sécurité
  resultats.securite = await auditSecurite(context, metier);
  // Audit qualité métier
  resultats.qualite = await auditQualite(context, metier);
  // Audit conformité réglementaire
  resultats.conformite = await auditConformite(context, metier);
  // Audit edge cases spécifiques Construction
  resultats.edgeCases = await auditEdgeCases(context, metier);
  // Génération du rapport d’audit consolidé
  const rapport = genererRapport(resultats, metier);
  // Traçabilité complète de l’audit
  tracerAudit(rapport, context, metier);
  return rapport;
}

module.exports = {
  auditCompletConstruction
};
