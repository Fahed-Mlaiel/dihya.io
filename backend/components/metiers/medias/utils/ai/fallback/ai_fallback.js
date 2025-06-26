// ai_fallback.js – Fallback AI open source pour Medias (medias)
module.exports = {
  aiFallback: (text, lang = 'fr') => {
    // Simule un fallback AI open source pour la traduction ou l'analyse
    if (!text) return '[AI-Fallback] Texte manquant';
    return `[AI-Fallback][${lang.toUpperCase()}] ${text}`;
  }
};
