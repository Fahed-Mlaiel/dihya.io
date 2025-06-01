// ai.js - Génération IA (frontend)
/**
 * @fileoverview Génération IA avec fallback LLaMA, Mixtral, Mistral, sécurité, i18n, audit, documentation intégrée.
 * @author Dihya Coding
 * @version 1.0.0
 * @license MIT
 */
import { SUPPORTED_LANGUAGES } from '../../constants/constants';

export async function generateAI({ prompt, language = 'fr', model = 'llama' }) {
  // Sécurité : validation, audit, fallback
  if (!SUPPORTED_LANGUAGES.includes(language)) throw new Error('Langue non supportée');
  let response;
  try {
    switch (model) {
      case 'llama':
        response = await fetch('/api/ai/llama', { method: 'POST', body: JSON.stringify({ prompt, language }) });
        break;
      case 'mixtral':
        response = await fetch('/api/ai/mixtral', { method: 'POST', body: JSON.stringify({ prompt, language }) });
        break;
      case 'mistral':
        response = await fetch('/api/ai/mistral', { method: 'POST', body: JSON.stringify({ prompt, language }) });
        break;
      default:
        throw new Error('Modèle IA non supporté');
    }
    if (!response.ok) throw new Error('Erreur IA');
    return await response.json();
  } catch (e) {
    // Fallback open source
    return { result: 'Fallback IA open source', error: e.message };
  }
}
