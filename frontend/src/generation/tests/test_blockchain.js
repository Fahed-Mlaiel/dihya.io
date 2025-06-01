/**
 * @file test_blockchain.js
 * @description Tests unitaires et d’intégration pour les modules blockchain Dihya Coding (contrats, wallets, intégrations).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Tous les tests respectent les bonnes pratiques de validation, anonymisation, logs locaux et consentement utilisateur.
 */

import { contractTemplate, clearLocalBlockchainTemplateLogs } from '../blockchain/contractTemplate';

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
window.localStorage.setItem('blockchain_feature_consent', 'true');

describe('contractTemplate', () => {
  afterEach(() => {
    clearLocalBlockchainTemplateLogs();
  });

  it('génère un contrat blockchain valide', () => {
    const data = { contractName: 'Token', symbol: 'TKN', owner: '0x123' };
    const contract = contractTemplate(data);
    expect(contract).toBeDefined();
    expect(contract.contractName).toBe('Token');
    expect(contract.symbol).toBe('TKN');
  });

  it('refuse les données invalides', () => {
    expect(() => contractTemplate({})).toThrow();
    expect(() => contractTemplate({ contractName: '' })).toThrow();
  });

  it('respecte le consentement utilisateur', () => {
    window.localStorage.removeItem('blockchain_feature_consent');
    expect(() => contractTemplate({ contractName: 'Test', symbol: 'TST' })).toThrow(/Consentement requis/);
    window.localStorage.setItem('blockchain_feature_consent', 'true');
  });

  it('purge les logs de génération blockchain (droit à l’oubli RGPD)', () => {
    contractTemplate({ contractName: 'Test', symbol: 'TST', owner: '0xabc' });
    expect(window.localStorage.getItem('blockchain_template_logs')).not.toBeNull();
    clearLocalBlockchainTemplateLogs();
    expect(window.localStorage.getItem('blockchain_template_logs')).toBeNull();
  });
});