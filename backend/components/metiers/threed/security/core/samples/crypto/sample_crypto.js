// sample_crypto.js – Exemple de clé/chiffrement clé en main

function getSampleCrypto() {
  return {
    key: '0123456789abcdef0123456789abcdef',
    iv: 'abcdef9876543210',
    algorithm: 'aes-256-cbc',
    example: 'données chiffrées...'
  };
}

module.exports = { getSampleCrypto };
