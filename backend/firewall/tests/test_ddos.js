// test_ddos.js – Tests du rate limiting (Jest)
const rateLimiter = require('../ddos/rate_limiter');
test('rateLimiter est une fonction', () => {
  expect(typeof rateLimiter).toBe('function');
});
