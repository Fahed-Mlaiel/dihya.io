/**
 * Log d'audit pour traçabilité des actions utilisateurs.
 */
export interface AuditLog {
  id: string;
  userId: string;
  action: string;
  timestamp: string;
  details?: object;
}

/**
 * Événement RGPD (export, anonymisation, suppression).
 */
export interface RgpdEvent {
  id: string;
  userId: string;
  type: 'export' | 'anonymisation' | 'suppression';
  date: string;
  status: 'pending' | 'completed' | 'failed';
}

/**
 * Log d'accès utilisateur (sécurité, conformité).
 */
export interface AccessLog {
  id: string;
  userId: string;
  ip: string;
  action: string;
  timestamp: string;
}
