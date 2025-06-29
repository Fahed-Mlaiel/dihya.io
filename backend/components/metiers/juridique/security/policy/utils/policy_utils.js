// policy_utils.js – Utilitaires pour politiques sécurité

const policyUtils = {
  describePolicy(model) {
    return `Politique: ${model.name} (v${model.version}) – Règles: ${model.rules.join(', ')}`;
  }
};

module.exports = { policyUtils };
