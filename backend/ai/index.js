/**
 * Dihya – AI Backend Index (Node.js)
 * ----------------------------------
 * Point d'entrée unique pour le moteur IA Node.js (multi-stack, multilingue, souveraineté, sécurité).
 * - Exporte le routeur Express IA ultra avancé (voir ai.js)
 * - Prêt pour intégration dans l'app principale, CI/CD, Codespaces, cloud souverain
 * - Documentation multilingue, RBAC, logs, fallback IA open source
 *
 * 🇫🇷 Point d'entrée backend IA Node.js (sécurité, fallback, multilingue)
 * 🇬🇧 Node.js AI backend entry point (secure, fallback, multilingual)
 * 🇦🇪 نقطة دخول محرك الذكاء الاصطناعي (Node.js) مع الأمان والدعم متعدد اللغات
 * ⵣ Amuddu n backend IA Node.js (amatu, fallback, multilingual)
 */

const aiRouter = require('./ai'); // ai.js = moteur IA Express prêt à l'emploi

module.exports = aiRouter;

// Utilisation dans l'app principale :
// const aiRouter = require('./backend/ai');
// app.use('/api/ai', aiRouter);

// Sécurité, logs, RBAC, fallback IA open source, multilingue, prêt CI/CD, Codespaces, production.
