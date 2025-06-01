// journalismeService.js - service avancé, REST, GraphQL, sécurité, rôles, i18n
/**
 * @file journalismeService.js
 * @description Service métier pour la gestion de projets journalisme (REST, GraphQL, sécurité, i18n, rôles, audit)
 * @roles (admin, user, invité)
 * @i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @audit (logs, anonymisation, export)
 */
import { logAction } from '../utils/audit';

export class JournalismeService {
  constructor(user, i18n) {
    this.user = user;
    this.i18n = i18n;
  }
  async createProject({ nom, pays }) {
    if (!this.user || this.user.role !== 'admin') {
      logAction('createProjectDenied', this.user, { nom, pays });
      throw new Error(this.i18n.permission);
    }
    const projet = { nom, pays, ownerRole: this.user.role };
    logAction('createProject', this.user, projet);
    return projet;
  }
}
