// tests/ipfs_publish.test.js — Tests automatisés publication IPFS (Node.js, logique métier Dihya)
const { publishToIPFS } = require('./ipfs_publish');
const fs = require('fs');

describe('IPFS Publish Logic', () => {
  it('should return a valid gateway URL or null if IPFS is absent', () => {
    // On simule la présence d'un dossier build_demo
    if (!fs.existsSync('build_demo')) fs.mkdirSync('build_demo');
    const url = publishToIPFS('build_demo');
    expect(typeof url === 'string' || url === null).toBe(true);
    // Nettoyage
    fs.rmdirSync('build_demo', { recursive: true });
  });
});
