// iaService.js - service avancé, REST, GraphQL, sécurité, rôles, i18n
/**
 * @file iaService.js
 * @description Service métier pour la gestion de projets IA (REST, GraphQL, sécurité, i18n, rôles, audit)
 * @roles (admin, user, invité)
 * @i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @audit (logs, anonymisation, export)
 */
import { logAction } from '../utils/audit';

export class IAService {
  constructor(user, i18n) {
    this.user = user;
    this.i18n = i18n;
  }
  async createProject({ name, type }) {
    if (!this.user || this.user.role !== 'admin') {
      logAction('createProjectDenied', this.user, { name, type });
      throw new Error(this.i18n.permission);
    }
    const project = { name, type, ownerRole: this.user.role };
    logAction('createProject', this.user, project);
    return project;
  }
}
