// onboarding_helper.js – Node.js helper pour onboarding sécurité vr_ar
function onboardingChecklist(user) {
  return [
    'Compte créé',
    'Accès sécurisé',
    'Formation RGPD suivie',
    `Utilisateur: ${user.name}`
  ];
}
module.exports = { onboardingChecklist };
