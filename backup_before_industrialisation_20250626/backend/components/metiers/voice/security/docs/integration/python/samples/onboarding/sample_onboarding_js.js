/* global console */
// Exemple avancé d’intégration Onboarding JS côté Python
import { onboardingHello } from '../../onboarding/onboarding_helper.js';

export function runOnboardingSample() {
  console.log('--- Onboarding Python Sample (JS) ---');
  console.log(onboardingHello());
}

if (require.main === module) {
  runOnboardingSample();
}
