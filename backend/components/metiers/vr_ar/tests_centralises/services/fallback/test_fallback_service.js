// Test avancé pour fallback.js du module services/fallback
// Remplacer l'import par le chemin réel si besoin
const { fallbackService } = require('../../../services/fallback/fallback_service');

describe('Services Fallback', () => {
  it('should expose fallbackService', () => {
    expect(typeof fallbackService).toBe('function');
  });

  it('should return fallback=true and empty=true if no data is provided', () => {
    const result = fallbackService();
    expect(result).toEqual({ fallback: true, empty: true });
  });

  it('should add fallback and status to provided data', () => {
    const data = { foo: 'bar' };
    const result = fallbackService(data);
    expect(result).toMatchObject({ foo: 'bar', fallback: true, status: 'fallback' });
  });

  it('should not mutate the original data object', () => {
    const data = { a: 1 };
    const copy = { ...data };
    fallbackService(data);
    expect(data).toEqual(copy);
  });

  it('should handle edge case: data is null', () => {
    const result = fallbackService(null);
    expect(result).toEqual({ fallback: true, empty: true });
  });

  it('should handle edge case: data is an empty object', () => {
    const result = fallbackService({});
    expect(result).toEqual({ fallback: true, status: 'fallback' });
  });

  it('should be robust to non-object types (string, number)', () => {
    expect(fallbackService('test')).toMatchObject({ fallback: true, status: 'fallback' });
    expect(fallbackService(123)).toMatchObject({ fallback: true, status: 'fallback' });
  });

  it('should be auditable (structure always includes fallback)', () => {
    const result = fallbackService({ foo: 'bar' });
    expect(result.fallback).toBe(true);
  });
});
