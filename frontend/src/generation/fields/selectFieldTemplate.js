// selectFieldTemplate.js - Template de champ select (frontend)
/**
 * @fileoverview Template de champ select, multilingue, sécurisé, documentation intégrée, exemple complet.
 * @author Dihya Coding
 * @version 1.0.0
 * @license MIT
 */
import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';

/**
 * Champ select générique.
 * @param {Object} props
 * @param {string} props.label
 * @param {string} props.value
 * @param {function} props.onChange
 * @param {Array<{label: string, value: string}>} props.options
 * @returns {JSX.Element}
 */
const SelectField = ({ label, value, onChange, options }) => {
  const { t } = useTranslation();
  return (
    <div>
      <label>{t(label)}</label>
      <select value={value} onChange={e => onChange(e.target.value)}>
        {options.map(opt => (
          <option key={opt.value} value={opt.value}>{t(opt.label)}</option>
        ))}
      </select>
    </div>
  );
};

SelectField.propTypes = {
  label: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
  options: PropTypes.arrayOf(PropTypes.shape({
    label: PropTypes.string.isRequired,
    value: PropTypes.string.isRequired,
  })).isRequired,
};

export default SelectField;
