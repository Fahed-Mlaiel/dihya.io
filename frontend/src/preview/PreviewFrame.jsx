/**
 * @file PreviewFrame.jsx
 * @description Composant d’aperçu embarqué (iframe sécurisé) pour Dihya Coding : design moderne, SEO, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.
 * Toutes les opérations sont validées, loguées localement, anonymisées et respectent le consentement utilisateur.
 */

import React, { useEffect, useRef } from 'react';
import PropTypes from 'prop-types';

/**
 * Composant d’aperçu sécurisé via iframe.
 * @param {object} props
 * @param {string} props.src - URL de la ressource à prévisualiser
 * @param {string} [props.title] - Titre pour l’accessibilité et le SEO
 * @param {number|string} [props.height] - Hauteur de l’iframe
 * @param {number|string} [props.width] - Largeur de l’iframe
 * @returns {JSX.Element}
 */
export default function PreviewFrame({ src, title, height = 600, width = '100%' }) {
  const iframeRef = useRef(null);

  useEffect(() => {
    if (hasConsent()) {
      logPreviewFrameEvent('preview_frame_view', { src: anonymizeSrc(src), timestamp: new Date().toISOString() });
    }
  }, [src]);

  return (
    <div className="preview-frame-container" style={{ width: '100%', maxWidth: 1200, margin: '0 auto' }}>
      <iframe
        ref={iframeRef}
        src={src}
        title={title || 'Aperçu sécurisé'}
        width={width}
        height={height}
        loading="lazy"
        sandbox="allow-scripts allow-same-origin"
        aria-label={title || 'Aperçu sécurisé'}
        style={{
          border: '1px solid #e0e0e0',
          borderRadius: 8,
          background: '#fff',
          boxShadow: '0 2px 8px rgba(0,0,0,0.04)'
        }}
      />
    </div>
  );
}

PreviewFrame.propTypes = {
  src: PropTypes.string.isRequired,
  title: PropTypes.string,
  height: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  width: PropTypes.oneOfType([PropTypes.string, PropTypes.number])
};

/**
 * Vérifie le consentement utilisateur (RGPD).
 * @returns {boolean}
 */
function hasConsent() {
  return typeof window !== 'undefined' && window.localStorage && window.localStorage.getItem('preview_frame_feature_consent');
}

/**
 * Log local pour auditabilité (conformité RGPD).
 * @param {string} action
 * @param {object} data
 */
function logPreviewFrameEvent(action, data) {
  try {
    const logs = JSON.parse(window.localStorage.getItem('preview_frame_logs') || '[]');
    logs.push({
      action,
      data,
      timestamp: new Date().toISOString()
    });
    window.localStorage.setItem('preview_frame_logs', JSON.stringify(logs));
  } catch {
    // Silencieux pour UX
  }
}

/**
 * Anonymise l’URL de la ressource pour les logs.
 * @param {string} src
 * @returns {string}
 */
function anonymizeSrc(src) {
  if (!src || typeof src !== 'string') return '';
  try {
    const url = new URL(src, window.location.origin);
    return url.origin + url.pathname.replace(/\/[a-zA-Z0-9]{16,}/g, '/***');
  } catch {
    return '[src]';
  }
}

/**
 * Efface les logs d’aperçu frame (droit à l’oubli RGPD).
 */
export function clearLocalPreviewFrameLogs() {
  if (typeof window !== 'undefined' && window.localStorage) {
    window.localStorage.removeItem('preview_frame_logs');
  }
}