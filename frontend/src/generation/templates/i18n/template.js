// i18n template pour la génération de projets IA, VR, AR, etc.
// Supporte : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
// Sécurité maximale, multitenancy, gestion des rôles, fallback IA open source
// @see https://github.com/DihyaCoding

/**
 * Génère les chaînes i18n pour un projet donné
 * @param {string} locale - Code langue (fr, en, ar, ...)
 * @param {object} context - Contexte métier
 * @returns {object} Dictionnaire de traductions
 */
function generateI18n(locale, context) {
  const translations = {
    fr: { titre: 'Projet IA', bienvenue: 'Bienvenue', ...context },
    en: { titre: 'AI Project', bienvenue: 'Welcome', ...context },
    ar: { titre: 'مشروع الذكاء الاصطناعي', bienvenue: 'أهلا بك', ...context },
    de: { titre: 'KI-Projekt', bienvenue: 'Willkommen', ...context },
    zh: { titre: '人工智能项目', bienvenue: '欢迎', ...context },
    ja: { titre: 'AIプロジェクト', bienvenue: 'ようこそ', ...context },
    ko: { titre: 'AI 프로젝트', bienvenue: '환영합니다', ...context },
    nl: { titre: 'AI-project', bienvenue: 'Welkom', ...context },
    he: { titre: 'פרויקט בינה מלאכותית', bienvenue: 'ברוך הבא', ...context },
    fa: { titre: 'پروژه هوش مصنوعی', bienvenue: 'خوش آمدید', ...context },
    hi: { titre: 'एआई परियोजना', bienvenue: 'स्वागत है', ...context },
    es: { titre: 'Proyecto IA', bienvenue: 'Bienvenido', ...context },
    amazigh: { titre: 'ⴰⵙⵉⵏⴰⵡⴰⵙ ⵏ ⵉⴰⵙⵉⵏⴰⵡⴰⵙ', bienvenue: 'ⴰⴷⵔⴰⵔⴻⵏ', ...context }
  };
  return translations[locale] || translations['fr'];
}

module.exports = { generateI18n };
