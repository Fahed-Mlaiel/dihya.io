// logger.test.js – Tests unitaires pour logger.js (Node.js/Jest)
const logger = require('./logger');
const fs = require('fs');
const path = require('path');

describe('Logger', () => {
  const logPath = path.join(__dirname, 'environnement.log');
  afterAll(() => { fs.existsSync(logPath) && fs.unlinkSync(logPath); });

  it('info écrit un log info', () => {
    logger.info('test info', { foo: 'bar' });
    const content = fs.readFileSync(logPath, 'utf-8');
    expect(content).toMatch('test info');
  });
  it('audit écrit un log audit', () => {
    logger.audit('test audit', { user: 'admin' });
    const content = fs.readFileSync(logPath, 'utf-8');
    expect(content).toMatch('test audit');
  });
});
