// helper_rgpd.js – Helpers RGPD (JS)
function anonymizeData(data) {
  return Object.fromEntries(Object.keys(data).map(k => [k, '***']));
}
module.exports = { anonymizeData };
