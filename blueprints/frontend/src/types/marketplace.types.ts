/**
 * Plugin métier installable via la marketplace.
 */
export interface Plugin {
  id: string;
  name: string;
  description: string;
  version: string;
  author: string;
  enabled: boolean;
  configSchema?: object;
}

/**
 * Élément de la marketplace (plugin ou template).
 */
export interface MarketplaceItem {
  id: string;
  name: string;
  type: 'plugin' | 'template';
  description: string;
  version: string;
  author: string;
  downloadUrl: string;
  tags?: string[];
}
