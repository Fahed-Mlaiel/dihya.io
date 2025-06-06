module.exports = {
  rootDir: '../../',
  testMatch: [
    '<rootDir>/frontend/src/components/metiers/**/*.test.js',
    '<rootDir>/frontend/src/tests/integration/**/*.js'
  ],
  moduleFileExtensions: ['js', 'jsx', 'json'],
  transform: {},
  testEnvironment: 'jsdom',
  collectCoverage: true,
  coverageDirectory: '<rootDir>/frontend/coverage',
  setupFilesAfterEnv: ['@testing-library/jest-dom/extend-expect'],
  moduleNameMapper: {
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy'
  }
};
