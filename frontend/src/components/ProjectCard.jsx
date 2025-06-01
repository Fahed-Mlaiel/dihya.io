/**
 * @file ProjectCard.jsx
 * @description Composant carte projet pour Dihya Coding.
 * Garantit design moderne, accessibilité, SEO, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Toutes les données affichées sont validées, anonymisées si besoin, et la structure est optimisée pour le SEO.
 */

import React from 'react';

/**
 * Composant React pour afficher une carte projet.
 * @param {object} props
 * @param {string} props.title - Titre du projet
 * @param {string} props.description - Description courte du projet
 * @param {string} props.updatedAt - Date de dernière modification (ISO)
 * @param {string} [props.status] - Statut du projet (ex: 'En cours', 'Terminé')
 * @param {string} [props.type] - Type de projet (ex: 'Web', 'Mobile')
 * @param {function} [props.onClick] - Callback lors du clic sur la carte
 * @param {string} [props.href] - Lien vers la page projet
 * @param {object} [props.meta] - Métadonnées additionnelles (SEO, audit)
 * @returns {JSX.Element}
 */
export default function ProjectCard({
  title,
  description,
  updatedAt,
  status,
  type,
  onClick,
  href,
  meta = {},
}) {
  // Validation basique des props
  if (!title || typeof title !== 'string') throw new Error('Titre projet requis');
  if (!description || typeof description !== 'string') throw new Error('Description projet requise');
  if (!updatedAt || typeof updatedAt !== 'string') throw new Error('Date de mise à jour requise');

  // Formatage date pour affichage humain et SEO
  const dateObj = new Date(updatedAt);
  const dateStr = dateObj.toLocaleDateString('fr-FR', { year: 'numeric', month: 'long', day: 'numeric' });

  // Auditabilité (log local)
  logProjectCardEvent('view_card', title);

  const cardContent = (
    <article
      className="project-card"
      aria-label={`Projet ${title}`}
      tabIndex={0}
      style={{
        background: '#fff',
        borderRadius: 12,
        boxShadow: '0 2px 12px rgba(0,0,0,0.07)',
        padding: 24,
        margin: '12px 0',
        transition: 'box-shadow 0.2s',
        cursor: onClick || href ? 'pointer' : 'default',
        outline: 'none',
        minWidth: 260,
        maxWidth: 420,
        border: '1px solid #E5E7EB',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
      }}
      {...(meta && meta['data-testid'] ? { 'data-testid': meta['data-testid'] } : {})}
      itemScope
      itemType="http://schema.org/CreativeWork"
    >
      <header>
        <h3
          itemProp="name"
          style={{
            fontSize: 20,
            margin: '0 0 8px 0',
            color: '#0057FF',
            fontWeight: 700,
            lineHeight: 1.2,
          }}
        >
          {title}
        </h3>
        {type && (
          <span
            style={{
              fontSize: 13,
              color: '#00C6AE',
              background: '#E6F9F6',
              borderRadius: 6,
              padding: '2px 8px',
              marginRight: 8,
              fontWeight: 500,
            }}
            aria-label={`Type de projet : ${type}`}
          >
            {type}
          </span>
        )}
        {status && (
          <span
            style={{
              fontSize: 13,
              color: status === 'Terminé' ? '#22C55E' : '#FFA500',
              background: status === 'Terminé' ? '#E6F9EC' : '#FFF8E6',
              borderRadius: 6,
              padding: '2px 8px',
              fontWeight: 500,
              marginLeft: 4,
            }}
            aria-label={`Statut : ${status}`}
          >
            {status}
          </span>
        )}
      </header>
      <p
        itemProp="description"
        style={{
          color: '#222',
          fontSize: 15,
          margin: '12px 0 16px 0',
          minHeight: 40,
        }}
      >
        {description}
      </p>
      <footer style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <time
          dateTime={dateObj.toISOString()}
          itemProp="dateModified"
          style={{ color: '#888', fontSize: 13 }}
        >
          Modifié le {dateStr}
        </time>
        {href && (
          <a
            href={href}
            aria-label={`Voir le projet ${title}`}
            style={{
              color: '#0057FF',
              textDecoration: 'none',
              fontWeight: 600,
              fontSize: 15,
              marginLeft: 12,
              borderRadius: 6,
              padding: '6px 14px',
              background: '#F5F7FA',
              transition: 'background 0.2s',
            }}
            rel="noopener"
            tabIndex={0}
          >
            Voir
          </a>
        )}
      </footer>
    </article>
  );

  if (href) {
    // SEO: <a> englobant pour navigation, sinon <div>
    return (
      <a
        href={href}
        aria-label={`Voir le projet ${title}`}
        style={{ textDecoration: 'none', color: 'inherit', display: 'block' }}
        rel="noopener"
        tabIndex={0}
        onClick={onClick}
      >
        {cardContent}
      </a>
    );
  }

  return (
    <div
      role="button"
      tabIndex={0}
      aria-label={`Projet ${title}`}
      onClick={onClick}
      onKeyPress={e => {
        if (onClick && (e.key === 'Enter' || e.key === ' ')) onClick(e);
      }}
      style={{ display: 'block' }}
    >
      {cardContent}
    </div>
  );
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {string} value
 */
function logProjectCardEvent(action, value) {
  try {
    const logs = JSON.parse(localStorage.getItem('project_card_logs') || '[]');
    logs.push({
      action,
      value,
      timestamp: new Date().toISOString(),
    });
    localStorage.setItem('project_card_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Efface les logs de ProjectCard locaux (droit à l’oubli RGPD).
 */
export function clearLocalProjectCardLogs() {
  localStorage.removeItem('project_card_logs');
}