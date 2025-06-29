// onboarding_helper.js – Node.js helper pour onboarding sécurité arts
function onboardingChecklist(user) {
  return [
    'Compte créé',
    'Accès sécurisé',
    'Formation RGPD suivie',
    `Utilisateur: ${user.name}`
  ];
}
module.exports = { onboardingChecklist };
