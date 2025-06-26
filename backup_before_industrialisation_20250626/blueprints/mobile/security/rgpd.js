// RGPD : suppression et anonymisation avancée, log audit
import { logAudit } from './audit';
export function anonymizeUser(user) {
  logAudit('anonymize', user);
  return { ...user, name: 'Anonyme', email: null };
}
export function deleteUser(user) {
  logAudit('delete', user);
  // Suppression simulée
  return true;
}
// Exemple d’intégration : anonymizeUser({name:'John',email:'john@dihya.io'})
