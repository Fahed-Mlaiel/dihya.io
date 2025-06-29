// onboarding_helper.js – Node.js helper pour onboarding sécurité education
function onboardingChecklist(user) {
  return [
    'Compte créé',
    'Accès sécurisé',
    'Formation RGPD suivie',
    `Utilisateur: ${user.name}`
  ];
}
module.exports = { onboardingChecklist };
