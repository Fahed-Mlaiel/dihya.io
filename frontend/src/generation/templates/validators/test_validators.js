import { auditValidation, validateSchema } from './template';

describe('Validators Template', () => {
  it('should validate schema correctly', () => {
    const schema = { foo: 'string', bar: 'number' };
    expect(validateSchema({ foo: 'abc', bar: 123 }, schema)).toBe(true);
    expect(validateSchema({ foo: 'abc', bar: 'nope' }, schema)).toBe(false);
  });

  it('should audit validation', () => {
    expect(() => auditValidation('TEST_VALIDATION', { foo: 'bar' })).not.toThrow();
  });
});
