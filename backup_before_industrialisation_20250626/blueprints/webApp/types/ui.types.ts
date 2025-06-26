/**
 * Page applicative (route, composant, sécurité).
 */
export interface Page {
  id: string;
  title: string;
  route: string;
  component: string;
  requiresAuth: boolean;
  rolesAllowed: string[];
}

/**
 * Composant UI typé selon atomic design (atom, molecule, organism, template).
 */
export interface UiComponent {
  id: string;
  name: string;
  type: 'atom' | 'molecule' | 'organism' | 'template';
  description?: string;
  propsSchema?: object;
}
