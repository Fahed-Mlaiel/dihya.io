/**
 * @file stacks.js
 * @description Constantes des stacks technologiques supportées par Dihya Coding.
 * Garantit design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Aucun secret, donnée personnelle ou sensible n’est stocké ici.
 */

/**
 * Liste des stacks technologiques disponibles pour la génération de projets.
 * Chaque stack est documentée pour l’UI, l’auditabilité et la conformité.
 * @readonly
 * @type {Array<{id: string, label: string, description: string, icon: string, tags: string[]}>}
 */
export const TECH_STACKS = [
  {
    id: 'mern',
    label: 'MERN (MongoDB, Express, React, Node)',
    description: 'Stack JavaScript moderne pour applications web fullstack, rapide et scalable.',
    icon: '🟩',
    tags: ['javascript', 'web', 'fullstack', 'mongo', 'react', 'node'],
  },
  {
    id: 'lamp',
    label: 'LAMP (Linux, Apache, MySQL, PHP)',
    description: 'Stack open-source classique pour hébergement web robuste et éprouvé.',
    icon: '🐧',
    tags: ['php', 'mysql', 'linux', 'apache', 'web'],
  },
  {
    id: 'jamstack',
    label: 'Jamstack (JavaScript, APIs, Markup)',
    description: 'Architecture moderne pour sites statiques, rapide, sécurisée et SEO-friendly.',
    icon: '⚡',
    tags: ['static', 'seo', 'javascript', 'api', 'markup'],
  },
  {
    id: 'python-flask',
    label: 'Python Flask',
    description: 'Framework léger pour API et applications web Python, extensible et rapide.',
    icon: '🐍',
    tags: ['python', 'flask', 'api', 'web'],
  },
  {
    id: 'django',
    label: 'Django',
    description: 'Framework Python complet pour applications web sécurisées et évolutives.',
    icon: '🌱',
    tags: ['python', 'django', 'web', 'secure'],
  },
  {
    id: 'spring',
    label: 'Spring Boot (Java)',
    description: 'Framework Java moderne pour microservices et applications web robustes.',
    icon: '☕',
    tags: ['java', 'spring', 'microservices', 'web'],
  },
  {
    id: 'dotnet',
    label: '.NET Core',
    description: 'Plateforme Microsoft pour applications web, APIs et microservices performants.',
    icon: '🟦',
    tags: ['dotnet', 'csharp', 'web', 'api', 'microsoft'],
  },
  {
    id: 'nextjs',
    label: 'Next.js',
    description: 'Framework React pour sites web statiques et dynamiques, optimisé SEO.',
    icon: '⏭️',
    tags: ['react', 'nextjs', 'seo', 'web'],
  },
  {
    id: 'vue',
    label: 'Vue.js',
    description: 'Framework JavaScript progressif pour interfaces web modernes et réactives.',
    icon: '🟩',
    tags: ['vue', 'javascript', 'web', 'frontend'],
  },
  {
    id: 'svelte',
    label: 'Svelte',
    description: 'Framework moderne pour interfaces web ultra-rapides et légères.',
    icon: '🔥',
    tags: ['svelte', 'javascript', 'web', 'frontend'],
  },
];

/**
 * Récupère la stack par son identifiant.
 * @param {string} id
 * @returns {object|null}
 */
export function getStackById(id) {
  return TECH_STACKS.find(stack => stack.id === id) || null;
}

/**
 * Vérifie si une stack est supportée.
 * @param {string} id
 * @returns {boolean}
 */
export function isValidStack(id) {
  return TECH_STACKS.some(stack => stack.id === id);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} stackId
 */
export function logStackEvent(action, stackId) {
  try {
    const logs = JSON.parse(localStorage.getItem('stack_logs') || '[]');
    logs.push({
      action,
      stackId,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('stack_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de stacks locaux (droit à l’oubli RGPD).
 */
export function clearLocalStackLogs() {
  localStorage.removeItem('stack_logs');
}