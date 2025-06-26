// helper_accessibility.js – Helpers d’accessibilité (JS)
function isAccessible(element) {
  return !!element.ariaLabel;
}
module.exports = { isAccessible };
