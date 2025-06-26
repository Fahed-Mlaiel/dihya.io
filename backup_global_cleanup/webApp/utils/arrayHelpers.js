/**
 * Supprime les doublons d'un tableau d'objets selon une clé
 * @param {Array} arr
 * @param {string} key
 * @returns {Array}
 */
export function uniqueBy(arr, key) {
  return [...new Map(arr.map(item => [item[key], item])).values()];
}

/**
 * Regroupe les éléments d'un tableau par une clé
 * @param {Array} arr
 * @param {string} key
 * @returns {Object}
 */
export function groupBy(arr, key) {
  return arr.reduce((acc, item) => {
    (acc[item[key]] = acc[item[key]] || []).push(item);
    return acc;
  }, {});
}
