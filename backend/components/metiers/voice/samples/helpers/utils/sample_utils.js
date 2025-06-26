// Exemple avancé d'utilitaire (Node.js)

module.exports = {
  sum: (a, b) => {
    if (a === null || b === null) return NaN;
    return a + b;
  },
  isEmpty: obj => {
    if (obj === null || obj === undefined) return false;
    if (Array.isArray(obj)) return obj.length === 0;
    if (typeof obj === 'object') return Object.keys(obj).length === 0;
    return true;
  }
};
