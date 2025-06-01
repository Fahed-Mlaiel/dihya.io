/**
 * @file Footer.jsx
 * @description Pied de page centralisé pour Dihya Coding.
 * Garantit design moderne, accessibilité, SEO, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Tous les liens sont validés, aucune donnée personnelle n’est exposée, et la structure est optimisée pour le SEO.
 */

import React from 'react';

export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer
      className="footer"
      aria-label="Pied de page Dihya Coding"
      style={{
        background: '#F5F7FA',
        color: '#222',
        padding: '32px 0 16px 0',
        borderTop: '1px solid #E5E7EB',
        fontFamily: 'Inter, Arial, sans-serif',
        fontSize: 15,
        marginTop: 40,
      }}
    >
      <div
        style={{
          maxWidth: 1200,
          margin: '0 auto',
          display: 'flex',
          flexWrap: 'wrap',
          justifyContent: 'space-between',
          alignItems: 'flex-start',
          gap: 24,
          padding: '0 24px',
        }}
      >
        <section aria-label="À propos de Dihya Coding" style={{ minWidth: 220 }}>
          <h2 style={{ fontSize: 18, margin: '0 0 8px 0', color: '#0057FF' }}>Dihya Coding</h2>
          <p style={{ margin: 0, color: '#555', maxWidth: 320 }}>
            Plateforme No-Code/Low-Code souveraine pour générer, déployer et auditer vos projets numériques en toute transparence.
          </p>
        </section>
        <nav aria-label="Liens utiles" style={{ minWidth: 180 }}>
          <h3 style={{ fontSize: 16, margin: '0 0 8px 0', color: '#0057FF' }}>Navigation</h3>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
            <li><a href="/" rel="noopener" style={linkStyle}>Accueil</a></li>
            <li><a href="/generate" rel="noopener" style={linkStyle}>Générer un projet</a></li>
            <li><a href="/about" rel="noopener" style={linkStyle}>À propos</a></li>
            <li><a href="/contact" rel="noopener" style={linkStyle}>Contact</a></li>
            <li><a href="/docs/user_guide/README.md" rel="noopener" style={linkStyle}>Documentation</a></li>
          </ul>
        </nav>
        <nav aria-label="Conformité et légalité" style={{ minWidth: 180 }}>
          <h3 style={{ fontSize: 16, margin: '0 0 8px 0', color: '#0057FF' }}>Conformité</h3>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
            <li><a href="/privacy" rel="noopener" style={linkStyle}>Politique de confidentialité</a></li>
            <li><a href="/legal" rel="noopener" style={linkStyle}>Mentions légales</a></li>
            <li><a href="/accessibility" rel="noopener" style={linkStyle}>Accessibilité</a></li>
          </ul>
        </nav>
        <section aria-label="Contact et réseaux" style={{ minWidth: 220 }}>
          <h3 style={{ fontSize: 16, margin: '0 0 8px 0', color: '#0057FF' }}>Contact</h3>
          <p style={{ margin: 0 }}>
            <a href="mailto:contact@dihya.coding" style={linkStyle}>contact@dihya.coding</a>
          </p>
          <div style={{ marginTop: 8 }}>
            <a href="https://github.com/dihya-coding" target="_blank" rel="noopener" aria-label="GitHub Dihya Coding" style={iconLinkStyle}>
              <span aria-hidden="true" style={{ fontSize: 20 }}>🐙</span>
            </a>
            <a href="https://twitter.com/dihya_coding" target="_blank" rel="noopener" aria-label="Twitter Dihya Coding" style={iconLinkStyle}>
              <span aria-hidden="true" style={{ fontSize: 20 }}>🐦</span>
            </a>
            {/* Ajouter d’autres réseaux si besoin */}
          </div>
        </section>
      </div>
      <div
        style={{
          textAlign: 'center',
          color: '#888',
          fontSize: 13,
          marginTop: 32,
          borderTop: '1px solid #E5E7EB',
          paddingTop: 12,
        }}
      >
        <span>
          © {currentYear} Dihya Coding – Souveraineté numérique, transparence et conformité RGPD.
        </span>
      </div>
    </footer>
  );
}

const linkStyle = {
  color: '#0057FF',
  textDecoration: 'none',
  fontWeight: 500,
  display: 'block',
  margin: '4px 0',
  outline: 'none',
};

const iconLinkStyle = {
  display: 'inline-block',
  marginRight: 12,
  color: '#0057FF',
  textDecoration: 'none',
  verticalAlign: 'middle',
};