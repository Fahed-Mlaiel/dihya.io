// Hook métier pour le parcours d’onboarding utilisateur
import { useState } from 'react';

const steps = [
  { title: 'Bienvenue', description: 'Découvrez la plateforme Dihya.io.' },
  { title: 'Créer un projet', description: 'Lancez votre premier projet No-Code.' },
  { title: 'Ajouter des plugins', description: 'Personnalisez avec des plugins métiers.' },
  { title: 'Générer & exporter', description: 'Générez et exportez votre application.' }
];

export function useOnboarding() {
  const [currentStep, setCurrentStep] = useState(0);
  const nextStep = () => setCurrentStep(s => Math.min(s + 1, steps.length - 1));
  const prevStep = () => setCurrentStep(s => Math.max(s - 1, 0));
  const resetOnboarding = () => setCurrentStep(0);
  return {
    step: steps[currentStep],
    currentStep,
    nextStep,
    prevStep,
    resetOnboarding,
    isLast: currentStep === steps.length - 1,
    isFirst: currentStep === 0
  };
}
