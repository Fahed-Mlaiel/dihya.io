// templates_helper.js
// Ultra-avancé, clé en main : helpers pour la gestion des templates/metiers/agriculture

const fs = require('fs');
const path = require('path');

/**
 * Rend un template à partir d'un contenu ou d'un chemin de fichier (absolu ou relatif).
 * Recherche le fichier dans l'ordre : chemin absolu, relatif au process, relatif au module appelant.
 */
function renderTemplate(template, variables) {
  if (typeof template === 'string') {
    // Absolu
    if (fs.existsSync(template)) {
      template = fs.readFileSync(template, 'utf8');
    } else {
      // Relatif au process
      const processPath = path.resolve(process.cwd(), template);
      if (fs.existsSync(processPath)) {
        template = fs.readFileSync(processPath, 'utf8');
      } else {
        // Relatif à l'appelant (stack)
        const stack = new Error().stack.split('\n');
        const callerLine = stack[2] || '';
        const match = callerLine.match(/\((.*):\d+:\d+\)/);
        if (match) {
          const callerDir = path.dirname(match[1]);
          const callerPath = path.resolve(callerDir, template);
          if (fs.existsSync(callerPath)) {
            template = fs.readFileSync(callerPath, 'utf8');
          }
        }
      }
    }
  }
  return template.replace(/{{\s*(\w+)\s*}}/g, (match, key) => {
    return key in variables ? variables[key] : match;
  });
}

/**
 * Vérifie si un template contient toutes les variables requises.
 * @param {string} template
 * @param {string[]} requiredVars
 * @returns {boolean}
 */
function hasRequiredVariables(template, requiredVars) {
  return requiredVars.every(v => new RegExp(`{{\\s*${v}\\s*}}`).test(template));
}

/**
 * Extrait toutes les variables {{var}} d'un template.
 * @param {string} template
 * @returns {string[]}
 */
function extractVariables(template) {
  const matches = template.match(/{{\s*(\w+)\s*}}/g) || [];
  return matches.map(m => m.replace(/{{\s*|\s*}}/g, ''));
}

/**
 * Nettoie un template en supprimant les variables non remplacées.
 * @param {string} template
 * @returns {string}
 */
function cleanTemplate(template) {
  return template.replace(/{{\s*\w+\s*}}/g, '');
}

function isValidTemplate(filename) {
  return /\.(html|j2|json|xml|txt)$/i.test(filename);
}

function mockTemplateContext() {
  return { model_name: 'TestModel', status: 'OK', date: new Date().toISOString() };
}

class TemplatesHelper {
  constructor() {
    this.config = {};
    this.auditTrail = [];
  }
  init(config) {
    this.config = config;
    this.auditTrail.push({ event: 'init', config, date: new Date().toISOString() });
    return true;
  }
  assist(operation, context) {
    if (!operation) throw new Error('Operation invalide');
    this.auditTrail.push({ event: 'assist', operation, context, date: new Date().toISOString() });
    return { success: true, operation, context };
  }
  getAuditTrail() {
    return this.auditTrail;
  }
}

module.exports = {
  TemplatesHelper,
  renderTemplate,
  hasRequiredVariables,
  extractVariables,
  cleanTemplate,
  isValidTemplate,
  mockTemplateContext,
};
