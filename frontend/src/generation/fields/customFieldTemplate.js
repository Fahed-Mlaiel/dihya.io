// customFieldTemplate.js - Template de champ personnalisé (frontend)
/**
 * @fileoverview Template de champ personnalisé, multilingue, sécurisé, documentation intégrée, exemple complet.
 * @author Dihya Coding
 * @version 1.0.0
 * @license MIT
 */
import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';

/**
 * Champ personnalisé générique.
 * @param {Object} props
 * @param {string} props.label
 * @param {string} props.value
 * @param {function} props.onChange
 * @returns {JSX.Element}
 */
const CustomField = ({ label, value, onChange }) => {
  const { t } = useTranslation();
  return (
    <div>
      <label>{t(label)}</label>
      <input type="text" value={value} onChange={e => onChange(e.target.value)} />
    </div>
  );
};

CustomField.propTypes = {
  label: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
};

export default CustomField;
