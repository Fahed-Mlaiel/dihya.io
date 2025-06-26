/**
 * Métadonnées SEO pour une page ou un composant.
 */
export interface SeoMeta {
  title: string;
  description: string;
  keywords: string[];
  image?: string;
  url?: string;
}

/**
 * Résultat de validation générique (helpers, forms, etc.).
 */
export interface ValidationResult {
  isValid: boolean;
  errors?: string[];
}

/**
 * Chaîne de date ISO 8601 (utilitaire).
 */
export type DateString = string;
