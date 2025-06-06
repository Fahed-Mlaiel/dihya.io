// guides/helpers/helpers_accessibility.js – Helpers avancés pour guides accessibilité

function validateAccessibilityConfig(config) {
  // Validation avancée de la config accessibilité
  if (!config || typeof config !== 'object') throw new Error('Config accessibilité invalide');
  if (!config.level || !['A','AA','AAA'].includes(config.level)) throw new Error('Niveau WCAG requis');
  return true;
}

// helpers_accessibility.js – Helpers ultra avancés accessibilité (JS)
module.exports = {
  checkAccessibility: (data) => {
    return data.contrast >= 7 && !!data.keyboard;
  },
  auditAccessibility: (data) => {
    let score = 0;
    if (data.contrast >= 7) score += 50;
    if (data.keyboard) score += 50;
    return { score, compliant: score === 100 };
  }
};

module.exports = { validateAccessibilityConfig };
