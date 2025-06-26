const paginate = (items, page, pageSize) => {
  const start = (page - 1) * pageSize;
  const end = start + pageSize;
  return items.slice(start, end);
};

test('pagination basic', () => {
  const items = Array.from({ length: 20 }, (_, i) => i + 1);
  expect(paginate(items, 1, 5)).toEqual([1, 2, 3, 4, 5]);
  expect(paginate(items, 2, 5)).toEqual([6, 7, 8, 9, 10]);
  expect(paginate(items, 4, 5)).toEqual([16, 17, 18, 19, 20]);
});

test('pagination empty', () => {
  expect(paginate([], 1, 5)).toEqual([]);
});

test('pagination out of range', () => {
  const items = Array.from({ length: 10 }, (_, i) => i + 1);
  expect(paginate(items, 3, 5)).toEqual([]);
});
