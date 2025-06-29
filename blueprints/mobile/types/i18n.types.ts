/**
 * Représente une locale supportée (langue, code, direction).
 */
export interface Locale {
  code: string; // ex: 'fr', 'en', 'ar', 'kab', etc.
  name: string;
  direction: 'ltr' | 'rtl';
}

/**
 * Message internationalisé (clé, valeur, description).
 */
export interface I18nMessage {
  key: string;
  value: string;
  description?: string;
}

/**
 * Ressource de traduction pour une locale donnée.
 */
export interface I18nResource {
  locale: Locale;
  messages: I18nMessage[];
}
