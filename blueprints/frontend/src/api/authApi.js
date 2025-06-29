// authApi.js
// API métier pour l’authentification et la gestion des sessions
import axios from 'axios';

export function login(credentials) {
  return axios.post('/api/auth/login', credentials);
}

export function logout() {
  return axios.post('/api/auth/logout');
}

export function getCurrentUser() {
  return axios.get('/api/auth/me');
}
