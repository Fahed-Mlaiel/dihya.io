const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const fs = require('fs');
const path = require('path');
const i18n = require('i18n');

// Configuration for i18n
i18n.configure({
  locales: ['en', 'fr', 'de', 'es'],
  directory: path.join(__dirname, '/locales'),
  defaultLocale: 'en',
  objectNotation: true,
  autoReload: true,
  updateFiles: false,
  syncFiles: false,
});

// Load RSA keys for JWT
const privateKey = fs.readFileSync(path.join(__dirname, 'private.key'), 'utf8');
const publicKey = fs.readFileSync(path.join(__dirname, 'public.key'), 'utf8');

const security = {
  encryptData: (data) => {
    const cipher = crypto.createCipher('aes-256-cbc', process.env.SECRET_KEY);
    let encrypted = cipher.update(JSON.stringify(data), 'utf8', 'hex');
    encrypted += cipher.final('hex');
    return encrypted;
  },

  decryptData: (encryptedData) => {
    const decipher = crypto.createDecipher('aes-256-cbc', process.env.SECRET_KEY);
    let decrypted = decipher.update(encryptedData, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    return JSON.parse(decrypted);
  },

  signToken: (payload) => {
    return jwt.sign(payload, privateKey, { algorithm: 'RS256', expiresIn: '1h' });
  },

  verifyToken: (token) => {
    try {
      return jwt.verify(token, publicKey, { algorithms: ['RS256'] });
    } catch (error) {
      throw new Error(i18n.__('error.invalid_token'));
    }
  },

  checkPermissions: (userRoles, requiredRoles) => {
    return requiredRoles.every(role => userRoles.includes(role));
  },

  handleGDPRCompliance: (userData) => {
    // Remove sensitive data for GDPR compliance
    delete userData.socialSecurityNumber;
    delete userData.creditCardInformation;
    // Add more fields as necessary
    return userData;
  },
};

module.exports = security;