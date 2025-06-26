const { arrayHelpers, dateHelpers } = require('../../../../../../blockchain/utils/index');
describe('arrayHelpers (helper)', () => {
  it('filtre les doublons dans un tableau', () => {
    expect(arrayHelpers.unique([1,2,2,3])).toEqual([1,2,3]);
  });
});
describe('dateHelpers (helper)', () => {
  it('formate une date ISO', () => {
    expect(dateHelpers.formatISO(new Date('2025-06-24T12:00:00Z'))).toBe('2025-06-24T12:00:00.000Z');
  });
});
