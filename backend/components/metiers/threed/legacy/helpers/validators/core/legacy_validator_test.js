// legacy_validator_test.js - Tests unitaires pour le validateur legacy Threed (JS)

const assert = require('assert');
const { isValidLegacyModel, auditLegacyData, isValidLegacyV2, isValidLegacyV3, auditLegacyStructure } = require('./legacy_validator');

describe('Legacy Validator', () => {
  it('should validate a correct legacy model', () => {
    assert(isValidLegacyModel({ legacy_id: 'l1', legacy_name: 'Ancien' }));
  });
  it('should audit legacy data', () => {
    assert(auditLegacyData({ legacy_id: 'l1', legacy_name: 'Ancien' }) === 'Legacy OK');
    assert(auditLegacyData({ legacy_name: 'Ancien' }).includes('Legacy ID manquant'));
  });
});

describe('Legacy Validator Advanced', () => {
  it('should validate legacy v2', () => {
    assert(isValidLegacyV2({ legacy_id: 'l2', version: 2 }));
  });
  it('should validate legacy v3', () => {
    assert(isValidLegacyV3({ legacy_id: 'l3', version: 3, meta: {} }));
  });
  it('should audit legacy structure', () => {
    assert(auditLegacyStructure({ legacy_id: 'l1', legacy_name: 'Ancien' }) === 'Legacy Structure OK');
    assert(auditLegacyStructure({ legacy_name: 'Ancien' }).includes('Legacy ID manquant'));
    assert(auditLegacyStructure({ legacy_id: 'l2', version: 2 }).includes('Meta manquant'));
  });
});

/**
 * Documentation intégrée :
 * - Tests multi-formats, edge cases, audit
 * - Utilisable pour migration massive, CI/CD
 */
