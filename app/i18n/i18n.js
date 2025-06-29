// Gestion principale de l’internationalisation

import fr from './fr.json';
import en from './en.json';
import ar from './ar.json';
import ber from './ber.json';
import de from './de.json';

const resources = { fr, en, ar, ber, de };

export function t(key, lang = 'fr') {
  return resources[lang]?.[key] || key;
}

export default resources;
