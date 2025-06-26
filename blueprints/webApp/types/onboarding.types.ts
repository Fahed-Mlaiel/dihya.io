/**
 * Étape d'onboarding utilisateur (progression, complétion).
 */
export interface OnboardingStep {
  id: string;
  title: string;
  description: string;
  order: number;
  completed: boolean;
}

/**
 * Guide métier multilingue (contenu, langue, mise à jour).
 */
export interface Guide {
  id: string;
  title: string;
  content: string;
  language: string;
  updatedAt: string;
}
