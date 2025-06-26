/**
 * Réponse standardisée d'une API (générique).
 */
export interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
  statusCode: number;
}

/**
 * Webhook externe (événement, URL, statut).
 */
export interface Webhook {
  id: string;
  url: string;
  event: string;
  isActive: boolean;
  createdAt: string;
}

/**
 * Statut d'un service métier (monitoring, healthcheck).
 */
export interface ServiceStatus {
  name: string;
  status: 'healthy' | 'degraded' | 'down';
  lastChecked: string;
  details?: string;
}

/**
 * Sauvegarde automatisée (local, cloud, IPFS).
 */
export interface Backup {
  id: string;
  type: 'local' | 'cloud' | 'ipfs';
  createdAt: string;
  status: 'pending' | 'completed' | 'failed';
  size: number;
}
