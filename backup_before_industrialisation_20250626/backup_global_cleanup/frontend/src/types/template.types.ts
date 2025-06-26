/**
 * Template métier prêt à l'emploi (secteur, champs dynamiques).
 */
export interface BusinessTemplate {
  id: string;
  name: string;
  sector: string;
  description: string;
  createdBy: string;
  createdAt: string;
  updatedAt: string;
  fields: TemplateField[];
}

/**
 * Champ d'un template métier (type, options, valeur par défaut).
 */
export interface TemplateField {
  name: string;
  type: string;
  required: boolean;
  defaultValue?: any;
  options?: any[];
}
