/* global console */
// Exemple avancé d’intégration Onboarding Node.js
import { onboardingHello } from '../../onboarding/onboarding_helper.js';

export function runOnboardingSample() {
  console.log('--- Onboarding Node.js Sample ---');
  console.log(onboardingHello());
}

if (require.main === module) {
  runOnboardingSample();
}
