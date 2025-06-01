import { getI18n, secureLog, validateInput } from './template';

describe('Utils Template', () => {
  it('should log securely', () => {
    expect(() => secureLog('TEST_EVENT', { foo: 'bar' }, 'info')).not.toThrow();
  });

  it('should return correct i18n', () => {
    expect(getI18n('fr').greeting).toBe('Bonjour');
    expect(getI18n('en').greeting).toBe('Hello');
    expect(getI18n('ar').greeting).toBe('مرحبا');
  });

  it('should validate input correctly', () => {
    const schema = { foo: 'string', bar: 'number' };
    expect(validateInput({ foo: 'abc', bar: 123 }, schema)).toBe(true);
    expect(validateInput({ foo: 'abc', bar: 'nope' }, schema)).toBe(false);
  });
});
