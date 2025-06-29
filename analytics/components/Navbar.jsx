import React, { useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { trackEvent } from '../analytics';
import PropTypes from 'prop-types';
import { NavLink } from 'react-router-dom';

const Navbar = ({ items }) => {
  const { t } = useTranslation();

  useEffect(() => {
    trackEvent('Navbar', 'view');
  }, []);

  return (
    <nav aria-label={t('navigation')}>
      <ul>
        {items.map((item, index) => (
          <li key={index}>
            <NavLink
              to={item.path}
              activeClassName="active"
              onClick={() => trackEvent('Navbar', 'click', item.label)}
            >
              {t(item.label)}
            </NavLink>
          </li>
        ))}
      </ul>
    </nav>
  );
};

Navbar.propTypes = {
  items: PropTypes.arrayOf(
    PropTypes.shape({
      path: PropTypes.string.isRequired,
      label: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default Navbar;