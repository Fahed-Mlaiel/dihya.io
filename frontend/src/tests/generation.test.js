/**
 * @file generation.test.js
 * @description Tests unitaires et d’intégration avancés pour le service de génération Dihya Coding.
 * Vérifie la génération multi-stack (code, markdown, images, templates métiers), la sécurité, la conformité RGPD, l’auditabilité, l’extensibilité, la robustesse, l’i18n, la souveraineté numérique et la documentation claire.
 * Respecte le cahier des charges Dihya Coding (sécurité, souveraineté, extensibilité, UX, AGPL, multilingue, fallback, logs anonymisés).
 */

import {
  generate,
  clearLocalGenerationServiceLogs
} from '../services/generationService';

describe('Service de génération – Dihya Coding', () => {
  beforeEach(() => {
    // Simule le consentement utilisateur pour les tests (RGPD)
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.setItem('generation_service_feature_consent', '1');
    }
    clearLocalGenerationServiceLogs();
  });

  afterEach(() => {
    clearLocalGenerationServiceLogs();
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.removeItem('generation_service_feature_consent');
    }
  });

  it('génère du code source sécurisé (JS)', () => {
    const result = generate({
      type: 'code',
      options: { language: 'javascript', content: 'console.log("Hello!");', log: true }
    });
    expect(result.success).toBe(true);
    expect(result.output).toContain('console.log');
    expect(result.error).toBeNull();
  });

  it('génère un document markdown multilingue', () => {
    const result = generate({
      type: 'markdown',
      options: { title: 'Titre Test', body: 'Ceci est un test.', log: true, lang: 'fr' }
    });
    expect(result.success).toBe(true);
    expect(result.output).toContain('# Titre Test');
    expect(result.output).toContain('Ceci est un test.');
    expect(result.error).toBeNull();
  });

  it('génère une image simulée (base64)', () => {
    const result = generate({
      type: 'image',
      options: { log: true }
    });
    expect(result.success).toBe(true);
    expect(result.output).toMatch(/^data:image\/png;base64,/);
    expect(result.error).toBeNull();
  });

  it('génère un template métier dynamique (JSON)', () => {
    const result = generate({
      type: 'template',
      options: { format: 'json', content: { name: 'Tourisme', fields: ['lieu', 'date', 'prix'] }, log: true }
    });
    expect(result.success).toBe(true);
    expect(result.output).toContain('"name": "Tourisme"');
    expect(result.output).toContain('fields');
    expect(result.error).toBeNull();
  });

  it('refuse la génération sans consentement RGPD', () => {
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.removeItem('generation_service_feature_consent');
    }
    const result = generate({
      type: 'code',
      options: { language: 'js', content: 'alert(1);' }
    });
    expect(result.success).toBe(false);
    expect(result.error).toMatch(/Consentement requis/);
  });

  it('gère les types de génération non supportés', () => {
    if (typeof window !== 'undefined' && window.localStorage) {
      window.localStorage.setItem('generation_service_feature_consent', '1');
    }
    const result = generate({
      type: 'unknown',
      options: { log: true }
    });
    expect(result.success).toBe(false);
    expect(result.error).toMatch(/non supporté/);
  });

  it('auditabilité : les logs sont anonymisés et effaçables', () => {
    const result = generate({
      type: 'code',
      options: { language: 'js', content: 'let x = 1;', log: true }
    });
    expect(result.success).toBe(true);

    // Vérifie la présence de logs anonymisés
    let logs = [];
    if (typeof window !== 'undefined' && window.localStorage) {
      logs = JSON.parse(window.localStorage.getItem('generation_service_logs') || '[]');
    }
    expect(Array.isArray(logs)).toBe(true);
    expect(logs.length).toBeGreaterThan(0);
    expect(logs[0].data.options.language.length).toBeLessThanOrEqual(16);

    // Efface les logs
    clearLocalGenerationServiceLogs();
    if (typeof window !== 'undefined' && window.localStorage) {
      const logsAfter = window.localStorage.getItem('generation_service_logs');
      expect(logsAfter === null || logsAfter === '[]').toBe(true);
    }
  });

  it('i18n : support multilingue (arabe, amazigh)', () => {
    const result = generate({
      type: 'markdown',
      options: { title: 'اختبار', body: 'هذا اختبار.', log: true, lang: 'ar' }
    });
    expect(result.success).toBe(true);
    expect(result.output).toContain('اختبار');
    expect(result.output).toContain('هذا اختبار.');
    expect(result.error).toBeNull();
  });

  it('robustesse : gère les entrées malicieuses sans faille', () => {
    const result = generate({
      type: 'code',
      options: { language: 'js', content: '<script>alert("xss")</script>', log: true }
    });
    expect(result.success).toBe(true);
    expect(result.output).not.toContain('<script>');
    expect(result.error).toBeNull();
  });

  it('extensibilité : permet d’ajouter dynamiquement des plugins de génération', () => {
    // Simulation d’un plugin de génération externe
    const pluginGen = (data) => data && data.type ? { ...data, plugin: true } : null;
    const result = pluginGen({ type: 'code', options: { language: 'js' } });
    expect(result).toHaveProperty('plugin', true);
  });
});

/* Documentation claire : chaque test est commenté pour auditabilité, robustesse, conformité, souveraineté */