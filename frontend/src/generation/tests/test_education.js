/**
 * @file test_education.js
 * @description Tests unitaires et d’intégration pour les modules éducatifs Dihya Coding (cours, quiz, évaluations, utilisateurs).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { educationTemplate, clearLocalEducationTemplateLogs } from '../education/template';

// Mock localStorage pour tests (si non disponible)
if (typeof window === 'undefined') {
  global.window = {};
}
if (!window.localStorage) {
  window.localStorage = {
    store: {},
    getItem(key) { return this.store[key] || null; },
    setItem(key, value) { this.store[key] = value; },
    removeItem(key) { delete this.store[key]; }
  };
}

// Consentement simulé pour les tests
window.localStorage.setItem('education_feature_consent', 'true');

describe('educationTemplate', () => {
  afterEach(() => {
    clearLocalEducationTemplateLogs();
  });

  it('génère un module cours valide', () => {
    const data = { course: { title: 'Maths' }, lessons: [{ title: 'Addition' }] };
    const module = educationTemplate({ type: 'course', data });
    expect(module.course).toBeDefined();
    expect(Array.isArray(module.lessons)).toBe(true);
    expect(module.course.title).toBe('Maths');
  });

  it('génère un module quiz valide', () => {
    const data = { quiz: { title: 'Quiz 1' }, questions: [{ q: '2+2?' }] };
    const module = educationTemplate({ type: 'quiz', data });
    expect(module.quiz).toBeDefined();
    expect(Array.isArray(module.questions)).toBe(true);
    expect(module.quiz.title).toBe('Quiz 1');
  });

  it('génère un module évaluation valide', () => {
    const data = { evaluation: { score: 18 }, feedback: 'Bravo' };
    const module = educationTemplate({ type: 'evaluation', data });
    expect(module.evaluation).toBeDefined();
    expect(module.feedback).toBe('Bravo');
  });

  it('génère un module utilisateur avec anonymisation', () => {
    const data = { user: { email: 'user@dihya.app', password: 'secret', name: 'Bob' } };
    const module = educationTemplate({ type: 'user', data });
    expect(module.user.email).toBe('[email]');
    expect(module.user.password).toBe('[protected]');
    expect(module.user.name).toBe('Bob');
  });

  it('refuse un type de module non supporté', () => {
    expect(() => educationTemplate({ type: 'unknown', data: {} })).toThrow();
  });

  it('refuse des données invalides', () => {
    expect(() => educationTemplate({ type: 'course', data: {} })).toThrow();
    expect(() => educationTemplate({ type: 'quiz', data: {} })).toThrow();
    expect(() => educationTemplate({ type: 'evaluation', data: {} })).toThrow();
    expect(() => educationTemplate({ type: 'user', data: {} })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('education_feature_consent');
    expect(() => educationTemplate({ type: 'course', data: { course: {}, lessons: [] } })).toThrow(/Consentement requis/);
    window.localStorage.setItem('education_feature_consent', 'true');
  });

  it('purge les logs de génération (droit à l’oubli RGPD)', () => {
    const data = { course: { title: 'Physique' }, lessons: [] };
    educationTemplate({ type: 'course', data });
    expect(window.localStorage.getItem('education_template_logs')).not.toBeNull();
    clearLocalEducationTemplateLogs();
    expect(window.localStorage.getItem('education_template_logs')).toBeNull();
  });
});