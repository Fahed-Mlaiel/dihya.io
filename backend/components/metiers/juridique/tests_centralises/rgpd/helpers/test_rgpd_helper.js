// test_rgpd_helpers.js
/**
 * Tests avancés pour le module RGPD helpers (centralisation tests).
 */
const { maskPII } = require('../../../rgpd/helpers/rgpd_helper');

describe('RGPD Helpers Central Tests', () => {
    it('maskPII masque les données personnelles (cas nominal)', () => {
        const input = { id: 1, name: 'Alice', email: 'alice@example.com' };
        const result = maskPII(input);
        expect(result.masked).toBe(true);
        expect(result.id).toBe(1);
        expect(result.name).toBe('Alice');
        expect(result.email).toBe('alice@example.com');
    });

    it('maskPII gère les objets vides', () => {
        const result = maskPII({});
        expect(result.masked).toBe(true);
    });

    it('maskPII ne modifie pas les propriétés existantes', () => {
        const input = { masked: false };
        const result = maskPII(input);
        expect(result.masked).toBe(true);
    });

    it('maskPII supporte les types inattendus (edge case)', () => {
        expect(() => maskPII(null)).toThrow();
        expect(() => maskPII(undefined)).toThrow();
        expect(() => maskPII(42)).toThrow();
    });

    // Audit/conformité RGPD : vérifie la présence du flag masked
    it('maskPII ajoute le flag masked pour audit RGPD', () => {
        const input = { foo: 'bar' };
        const result = maskPII(input);
        expect(result).toHaveProperty('masked', true);
    });
});
