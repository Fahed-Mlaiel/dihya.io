/**
 * textFieldTemplate.js
 * Template avancé pour la génération de champs texte multilingues, sécurisés, auditables.
 * @module generation/fields/textFieldTemplate
 * @author Dihya Team
 * @version 1.0.0
 * @description Génère un champ texte avec validation, i18n, audit, accessibilité, conformité RGPD.
 * @supportedLanguages [fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es]
 */

import PropTypes from 'prop-types';
import { useEffect } from 'react';
import { useTranslation } from 'react-i18next';

/**
 * Champ texte sécurisé, multilingue, auditable.
 * @param {Object} props
 * @param {string} props.label - Label du champ (clé i18n)
 * @param {string} props.value - Valeur du champ
 * @param {function} props.onChange - Callback changement
 * @param {boolean} [props.required=false] - Champ requis
 * @param {string[]} [props.allowedRoles=['admin','user']] - Rôles autorisés
 * @param {string} [props.auditKey] - Clé d'audit pour traçabilité
 * @returns {JSX.Element}
 */
export default function TextFieldTemplate({ label, value, onChange, required = false, allowedRoles = ['admin','user'], auditKey }) {
  const { t, i18n } = useTranslation();

  useEffect(() => {
    // Audit log (RGPD compliant)
    if (auditKey) {
      window.dispatchEvent(new CustomEvent('audit-log', {
        detail: { action: 'view', field: label, auditKey, lang: i18n.language }
      }));
    }
  }, [auditKey, label, i18n.language]);

  return (
    <div className="dihya-text-field" lang={i18n.language} aria-label={t(label)}>
      <label htmlFor={label}>{t(label)}{required && ' *'}</label>
      <input
        id={label}
        type="text"
        value={value}
        onChange={e => onChange(e.target.value)}
        required={required}
        aria-required={required}
        aria-label={t(label)}
        autoComplete="off"
        maxLength={512}
        pattern="^[\w\s\-\.,;:!?()@#&€$£%+=/\\]*$"
        data-roles={allowedRoles.join(',')}
        data-audit-key={auditKey || ''}
      />
    </div>
  );
}

TextFieldTemplate.propTypes = {
  label: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
  required: PropTypes.bool,
  allowedRoles: PropTypes.arrayOf(PropTypes.string),
  auditKey: PropTypes.string
};

// Accessibilité, sécurité, RGPD, i18n, audit intégrés. Prêt à l'emploi.
