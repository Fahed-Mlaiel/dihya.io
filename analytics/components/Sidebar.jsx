// components/Sidebar.jsx
import React from 'react';
import { NavLink } from 'react-router-dom';
import PropTypes from 'prop-types';

const analyticsModules = [
  { name: 'Backend', path: '/analytics/backend' },
  { name: 'Frontend', path: '/analytics/frontend' },
  { name: 'Plugins', path: '/analytics/plugins' },
  { name: 'Docs', path: '/analytics/docs' },
  { name: 'i18n', path: '/analytics/i18n' },
];

const Sidebar = ({ currentModule }) => {
  return (
    <aside className="sidebar">
      <nav className="nav">
        <ul className="nav-list">
          {analyticsModules.map((module) => (
            <li key={module.name} className={currentModule === module.name ? 'active' : ''}>
              <NavLink to={module.path} activeClassName="active">
                {module.name}
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  );
};

Sidebar.propTypes = {
  currentModule: PropTypes.string.isRequired,
};

export default Sidebar;