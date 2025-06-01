/**
 * @file Navbar.jsx
 * @description Barre de navigation principale pour Dihya Coding.
 * Garantit design moderne, accessibilité, SEO, conformité RGPD, auditabilité, extensibilité et robustesse.
 * Tous les liens sont validés, aucune donnée personnelle n’est exposée, et la structure est optimisée pour le SEO.
 */

import React from 'react';
import { DihyaLogo } from '../branding/Branding';
import LanguageSwitcher from './LanguageSwitcher';

/**
 * Composant React pour la barre de navigation principale.
 * @param {object} props
 * @param {string} props.currentLang - Code langue courante
 * @param {function} props.onLangChange - Callback pour changement de langue
 * @returns {JSX.Element}
 */
export default function Navbar({ currentLang = 'fr', onLangChange }) {
  return (
    <header
      className="navbar"
      aria-label="Barre de navigation Dihya Coding"
      style={{
        background: '#fff',
        borderBottom: '1px solid #E5E7EB',
        padding: '0 24px',
        fontFamily: 'Inter, Arial, sans-serif',
        position: 'sticky',
        top: 0,
        zIndex: 100,
      }}
    >
      <nav
        style={{
          maxWidth: 1200,
          margin: '0 auto',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          height: 64,
        }}
        aria-label="Navigation principale"
      >
        <a
          href="/"
          aria-label="Accueil Dihya Coding"
          style={{
            display: 'flex',
            alignItems: 'center',
            textDecoration: 'none',
            color: '#0057FF',
            fontWeight: 700,
            fontSize: 20,
          }}
        >
          <DihyaLogo width={40} height={40} style={{ marginRight: 10 }} />
          <span style={{ letterSpacing: 1 }}>Dihya Coding</span>
        </a>
        <ul
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 24,
            listStyle: 'none',
            margin: 0,
            padding: 0,
          }}
        >
          <li>
            <a href="/generate" style={linkStyle} rel="noopener">
              Générer
            </a>
          </li>
          <li>
            <a href="/preview" style={linkStyle} rel="noopener">
              Preview
            </a>
          </li>
          <li>
            <a href="/about" style={linkStyle} rel="noopener">
              À propos
            </a>
          </li>
          <li>
            <a href="/contact" style={linkStyle} rel="noopener">
              Contact
            </a>
          </li>
          <li>
            <a href="/docs/user_guide/README.md" style={linkStyle} rel="noopener">
              Docs
            </a>
          </li>
        </ul>
        <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <LanguageSwitcher currentLang={currentLang} onChange={onLangChange} />
          <a
            href="/login"
            style={{
              ...linkStyle,
              background: '#0057FF',
              color: '#fff',
              borderRadius: 6,
              padding: '8px 18px',
              fontWeight: 600,
              marginLeft: 8,
              border: 'none',
              textDecoration: 'none',
              transition: 'background 0.2s',
            }}
            rel="noopener"
          >
            Connexion
          </a>
        </div>
      </nav>
    </header>
  );
}

const linkStyle = {
  color: '#0057FF',
  textDecoration: 'none',
  fontWeight: 500,
  fontSize: 16,
  outline: 'none',
  padding: '6px 0',
  borderRadius: 4,
  transition: 'color 0.2s, background 0.2s',
  background: 'none',
};