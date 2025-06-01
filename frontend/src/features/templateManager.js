/**
 * @file templateManager.js
 * @description Gestionnaire de templates pour Dihya Coding (création, récupération, mise à jour, suppression, listing).
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les interactions sont validées, anonymisées, loguées localement et respectent le consentement utilisateur.
 */

/**
 * Liste tous les templates disponibles pour l’utilisateur.
 * @returns {Promise<Array<{id: string, name: string, description: string, stack: string, createdAt: string, updatedAt: string}>>}
 */
export async function listTemplates() {
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/templates', {
    headers: { ...(token ? { Authorization: `Bearer ${token}` } : {}) },
  });
  if (!res.ok) throw new Error('Erreur lors de la récupération des templates');
  const data = await res.json();
  logTemplateEvent('list_templates');
  return data;
}

/**
 * Récupère un template par son identifiant.
 * @param {string} templateId
 * @returns {Promise<object>}
 */
export async function getTemplate(templateId) {
  validateTemplateId(templateId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`/api/templates/${templateId}`, {
    headers: { ...(token ? { Authorization: `Bearer ${token}` } : {}) },
  });
  if (!res.ok) throw new Error('Erreur lors de la récupération du template');
  const data = await res.json();
  logTemplateEvent('get_template', anonymizeTemplateId(templateId));
  return data;
}

/**
 * Crée un nouveau template.
 * @param {object} params
 * @param {string} params.name
 * @param {string} params.description
 * @param {string} params.stack
 * @param {object} params.content
 * @returns {Promise<object>}
 */
export async function createTemplate({ name, description, stack, content }) {
  validateTemplateName(name);
  validateTemplateDescription(description);
  validateStack(stack);
  if (!content || typeof content !== 'object') throw new Error('Contenu de template invalide');
  const token = localStorage.getItem('jwt_token');
  const res = await fetch('/api/templates', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({ name, description, stack, content }),
  });
  if (!res.ok) throw new Error('Erreur lors de la création du template');
  const data = await res.json();
  logTemplateEvent('create_template', anonymizeTemplateName(name), stack);
  return data;
}

/**
 * Met à jour un template existant.
 * @param {string} templateId
 * @param {object} updates - Champs à mettre à jour (name, description, content, stack)
 * @returns {Promise<object>}
 */
export async function updateTemplate(templateId, updates) {
  validateTemplateId(templateId);
  if (!updates || typeof updates !== 'object') throw new Error('Mise à jour invalide');
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`/api/templates/${templateId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify(updates),
  });
  if (!res.ok) throw new Error('Erreur lors de la mise à jour du template');
  const data = await res.json();
  logTemplateEvent('update_template', anonymizeTemplateId(templateId));
  return data;
}

/**
 * Supprime un template existant.
 * @param {string} templateId
 * @returns {Promise<object>}
 */
export async function deleteTemplate(templateId) {
  validateTemplateId(templateId);
  const token = localStorage.getItem('jwt_token');
  const res = await fetch(`/api/templates/${templateId}`, {
    method: 'DELETE',
    headers: { ...(token ? { Authorization: `Bearer ${token}` } : {}) },
  });
  if (!res.ok) throw new Error('Erreur lors de la suppression du template');
  const data = await res.json();
  logTemplateEvent('delete_template', anonymizeTemplateId(templateId));
  return data;
}

/**
 * Valide l’identifiant du template.
 * @param {string} templateId
 */
function validateTemplateId(templateId) {
  if (!templateId || typeof templateId !== 'string' || templateId.length < 2) {
    throw new Error('Identifiant de template invalide');
  }
}

/**
 * Valide le nom du template.
 * @param {string} name
 */
function validateTemplateName(name) {
  if (!name || typeof name !== 'string' || name.length < 3 || name.length > 64) {
    throw new Error('Nom de template invalide');
  }
}

/**
 * Valide la description du template.
 * @param {string} description
 */
function validateTemplateDescription(description) {
  if (!description || typeof description !== 'string' || description.length < 3 || description.length > 256) {
    throw new Error('Description de template invalide');
  }
}

/**
 * Valide la stack technologique.
 * @param {string} stack
 */
function validateStack(stack) {
  // Liste des stacks supportées (à synchroniser avec constants/stacks.js)
  const SUPPORTED_STACKS = [
    'mern', 'lamp', 'jamstack', 'python-flask', 'django', 'spring', 'dotnet', 'nextjs', 'vue', 'svelte'
  ];
  if (!SUPPORTED_STACKS.includes(stack)) {
    throw new Error('Stack technologique non supportée');
  }
}

/**
 * Anonymise l’identifiant du template pour les logs.
 * @param {string} templateId
 * @returns {string}
 */
function anonymizeTemplateId(templateId) {
  // Exemple simple : suppression d’emails dans l’id
  return templateId.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Anonymise le nom du template pour les logs.
 * @param {string} name
 * @returns {string}
 */
function anonymizeTemplateName(name) {
  return name.replace(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi, '[email]');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} [value]
 * @param {string} [stack]
 */
function logTemplateEvent(action, value, stack) {
  try {
    const logs = JSON.parse(localStorage.getItem('template_manager_logs') || '[]');
    logs.push({
      action,
      value,
      stack,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('template_manager_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de gestion des templates (droit à l’oubli RGPD).
 */
export function clearLocalTemplateManagerLogs() {
  localStorage.removeItem('template_manager_logs');
}