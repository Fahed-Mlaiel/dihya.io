/**
 * Erreur de validation d'un champ de formulaire.
 */
export interface FormError {
  field: string;
  message: string;
}

/**
 * Champ de formulaire typé (label, type, options).
 */
export interface FormField {
  name: string;
  label: string;
  type: string;
  value?: any;
  required: boolean;
  options?: any[];
}

/**
 * Schéma de formulaire (ensemble de champs).
 */
export interface FormSchema {
  fields: FormField[];
}
