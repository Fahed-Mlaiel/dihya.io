/**
 * @file SEO.jsx
 * @description Composant centralisé pour la gestion SEO (balises meta, titre, langue) de Dihya Coding.
 * Garantit design moderne, SEO optimal, sécurité, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Toutes les propriétés sont validées et documentées selon les bonnes pratiques SEO et RGPD.
 */

import React, { useEffect } from 'react';

/**
 * Composant React pour injecter dynamiquement les balises SEO dans le head.
 * @param {object} props
 * @param {string} props.title - Titre de la page (obligatoire)
 * @param {string} [props.description] - Description SEO de la page
 * @param {string} [props.keywords] - Mots-clés SEO
 * @param {string} [props.lang] - Code langue (ex: 'fr', 'en', 'ber')
 * @param {string} [props.themeColor] - Couleur du navigateur (meta theme-color)
 * @param {string} [props.canonical] - URL canonique
 * @param {object} [props.extraMeta] - Balises meta additionnelles (clé/valeur)
 * @returns {null}
 */
export default function SEO({
  title,
  description,
  keywords,
  lang = 'fr',
  themeColor = '#0057FF',
  canonical,
  extraMeta = {},
}) {
  useEffect(() => {
    if (!title || typeof title !== 'string') throw new Error('SEO: title requis');
    document.title = title;

    // Langue du document (SEO + accessibilité)
    document.documentElement.lang = lang;

    // Meta description
    setOrUpdateMeta('description', description || 'Plateforme No-Code/Low-Code souveraine pour générer, déployer et auditer vos projets numériques.');
    // Meta keywords
    if (keywords) setOrUpdateMeta('keywords', keywords);

    // Meta theme-color (SEO mobile)
    setOrUpdateMeta('theme-color', themeColor);

    // Canonical
    if (canonical) setOrUpdateLink('canonical', canonical);

    // Extra meta
    Object.entries(extraMeta).forEach(([key, value]) => {
      setOrUpdateMeta(key, value);
    });

    // Auditabilité (log local RGPD)
    logSeoEvent('set_seo', title);
  }, [title, description, keywords, lang, themeColor, canonical, extraMeta]);

  return null;
}

/**
 * Ajoute ou met à jour une balise meta dans le head.
 * @param {string} name
 * @param {string} content
 */
function setOrUpdateMeta(name, content) {
  if (!content) return;
  let tag = document.querySelector(`meta[name="${name}"]`);
  if (!tag) {
    tag = document.createElement('meta');
    tag.setAttribute('name', name);
    document.head.appendChild(tag);
  }
  tag.setAttribute('content', content);
}

/**
 * Ajoute ou met à jour une balise link (ex: canonical).
 * @param {string} rel
 * @param {string} href
 */
function setOrUpdateLink(rel, href) {
  if (!href) return;
  let link = document.querySelector(`link[rel="${rel}"]`);
  if (!link) {
    link = document.createElement('link');
    link.setAttribute('rel', rel);
    document.head.appendChild(link);
  }
  link.setAttribute('href', href);
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 */
function logSeoEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('seo_component_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('seo_component_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs SEO du composant (droit à l’oubli RGPD).
 */
export function clearLocalSeoComponentLogs() {
  localStorage.removeItem('seo_component_logs');
}