// dateFieldTemplate.js - Template de champ date (frontend)
/**
 * @fileoverview Template de champ date, multilingue, sécurisé, documentation intégrée, exemple complet.
 * @author Dihya Coding
 * @version 1.0.0
 * @license MIT
 */
import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';

/**
 * Champ date générique.
 * @param {Object} props
 * @param {string} props.label
 * @param {string} props.value
 * @param {function} props.onChange
 * @returns {JSX.Element}
 */
const DateField = ({ label, value, onChange }) => {
  const { t } = useTranslation();
  return (
    <div>
      <label>{t(label)}</label>
      <input type="date" value={value} onChange={e => onChange(e.target.value)} />
    </div>
  );
};

DateField.propTypes = {
  label: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
};

export default DateField;
