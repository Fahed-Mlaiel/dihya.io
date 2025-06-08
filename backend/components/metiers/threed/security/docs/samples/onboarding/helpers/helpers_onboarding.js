// helpers_onboarding.js
// Helpers avancés pour le parcours utilisateur, sécurité à l’entrée

function startOnboarding(user) {
  // Simule le début d'un onboarding sécurisé
  return { ...user, onboardingStarted: true, startedAt: new Date().toISOString() };
}

function completeOnboarding(user) {
  // Simule la complétion d'un onboarding
  return { ...user, onboardingCompleted: true, completedAt: new Date().toISOString() };
}

module.exports = { startOnboarding, completeOnboarding };
