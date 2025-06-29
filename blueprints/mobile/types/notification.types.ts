/**
 * Notification utilisateur (push, email, etc.).
 */
export interface Notification {
  id: string;
  userId: string;
  type: NotificationType;
  message: string;
  read: boolean;
  createdAt: string;
}

/**
 * Types de notifications supportés.
 */
export type NotificationType = 'info' | 'success' | 'warning' | 'error';

/**
 * Événement analytics (tracking, usage, etc.).
 */
export interface AnalyticsEvent {
  id: string;
  userId?: string;
  event: string;
  properties?: object;
  timestamp: string;
}
