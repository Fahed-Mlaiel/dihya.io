export function isAuthenticated() {
  const token = localStorage.getItem('token');
  return !!token;
}
export function getUserRole() {
  const token = localStorage.getItem('token');
  if (!token) return 'guest';
  if (token === 'jwt.token.exemple') return 'admin';
  return 'user';
}
export function hasPermission(role, permission) {
  const permissions = { admin: ['read', 'write', 'delete'], user: ['read', 'write'], guest: ['read'] };
  return permissions[role]?.includes(permission);
}