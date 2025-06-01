import { render } from '@testing-library/react';
import { SeoMeta } from './index';

describe('SeoMeta métier (ultra avancé)', () => {
  const baseProps = {
    lang: 'fr',
    title: 'Titre Test',
    description: 'Desc Test',
    url: 'https://test.com',
    image: 'https://test.com/img.png',
    type: 'website',
    tenant: 't1',
    role: 'admin'
  };

  it('génère toutes les balises SEO multilingues', () => {
    ['fr', 'en', 'ar', 'de'].forEach(lang => {
      const { container } = render(<SeoMeta {...baseProps} lang={lang} />);
      expect(container.querySelector('meta[name="robots"]')).toBeTruthy();
      expect(container.querySelector('meta[property="og:title"]')).toHaveAttribute('content', 'Titre Test');
    });
  });

  it('loggue les accès SEO structurés (window.dihyaSEOLog)', () => {
    window.dihyaSEOLog = [];
    render(<SeoMeta {...baseProps} />);
    expect(window.dihyaSEOLog.length).toBeGreaterThan(0);
    expect(window.dihyaSEOLog[0]).toMatchObject({ lang: 'fr', title: 'Titre Test', url: 'https://test.com', tenant: 't1', role: 'admin' });
  });

  it('respecte RGPD (pas de fuite de props sensibles)', () => {
    const { container } = render(<SeoMeta {...baseProps} tenant="secret-tenant" />);
    expect(container.innerHTML).not.toMatch(/secret-tenant/);
  });
});
