// Déclaration TypeScript avancée pour la documentation d'API
export interface ApiDoc {
  title: string;
  description: string;
  version: string;
  endpoints: Array<{ path: string; method: string; description: string }>;
}
