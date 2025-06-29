/**
 * Représente un utilisateur du système.
 * @interface User
 * @property {string} id - Identifiant unique de l'utilisateur
 * @property {string} name - Nom complet
 * @property {string} email - Adresse email
 * @property {UserRole} role - Rôle de l'utilisateur
 * @property {boolean} isActive - Statut d'activation
 * @property {string} createdAt - Date de création (ISO 8601)
 * @property {string} updatedAt - Date de mise à jour (ISO 8601)
 */
export interface User {
  id: string;
  name: string;
  email: string;
  role: UserRole;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
}

/**
 * Enumération des rôles utilisateurs standards.
 */
export type UserRole = 'admin' | 'user' | 'guest';

/**
 * Permission attribuable à un rôle ou utilisateur.
 */
export interface Permission {
  id: string;
  name: string;
  description?: string;
}

/**
 * Rôle utilisateur avec permissions associées.
 */
export interface Role {
  id: string;
  name: UserRole;
  permissions: Permission[];
}
