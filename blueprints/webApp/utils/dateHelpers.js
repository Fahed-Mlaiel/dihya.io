/**
 * Formate une date en chaîne lisible locale
 * @param {Date|string|number} date
 * @returns {string}
 */
export function formatDate(date) {
  return new Date(date).toLocaleDateString();
}

/**
 * Calcule la différence en jours entre deux dates
 * @param {Date|string|number} date1
 * @param {Date|string|number} date2
 * @returns {number}
 */
export function daysBetween(date1, date2) {
  const d1 = new Date(date1);
  const d2 = new Date(date2);
  return Math.floor(Math.abs(d2 - d1) / (1000 * 60 * 60 * 24));
}
