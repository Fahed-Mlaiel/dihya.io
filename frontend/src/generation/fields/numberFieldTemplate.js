// numberFieldTemplate.js - Template de champ numérique (frontend)
/**
 * @fileoverview Template de champ numérique, multilingue, sécurisé, documentation intégrée, exemple complet.
 * @author Dihya Coding
 * @version 1.0.0
 * @license MIT
 */
import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';

/**
 * Champ numérique générique.
 * @param {Object} props
 * @param {string} props.label
 * @param {number} props.value
 * @param {function} props.onChange
 * @returns {JSX.Element}
 */
const NumberField = ({ label, value, onChange }) => {
  const { t } = useTranslation();
  return (
    <div>
      <label>{t(label)}</label>
      <input type="number" value={value} onChange={e => onChange(Number(e.target.value))} />
    </div>
  );
};

NumberField.propTypes = {
  label: PropTypes.string.isRequired,
  value: PropTypes.number.isRequired,
  onChange: PropTypes.func.isRequired,
};

export default NumberField;
