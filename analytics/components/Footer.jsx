import React from 'react';
import PropTypes from 'prop-types';
import { useTranslation } from 'react-i18next';
import { trackEvent } from '../analytics/AnalyticsService'; // Hypothetical analytics service module

const Footer = ({ onPrivacyPolicyClick }) => {
  const { t } = useTranslation();

  const handleLinkClick = (linkType) => {
    trackEvent({
      category: 'Footer',
      action: 'click',
      label: linkType,
    });
  };

  return (
    <footer aria-labelledby="footer-heading" className="footer">
      <h2 id="footer-heading" className="visually-hidden">
        {t('footer.heading')}
      </h2>
      <nav>
        <ul className="footer-links">
          <li>
            <a
              href="#"
              onClick={() => {
                handleLinkClick('privacy');
                onPrivacyPolicyClick();
              }}
              aria-label={t('footer.privacyPolicy')}
            >
              {t('footer.privacyPolicy')}
            </a>
          </li>
          {/* Additional footer links can be added here */}
        </ul>
      </nav>
    </footer>
  );
};

Footer.propTypes = {
  onPrivacyPolicyClick: PropTypes.func.isRequired,
};

export default Footer;