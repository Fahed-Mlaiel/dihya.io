import { render, screen } from '@testing-library/react';
import { I18nextProvider } from 'react-i18next';
import i18n from '../../../../i18nTestConfig';
import BlockchainDashboard from './index';

describe('BlockchainDashboard métier (ultra avancé)', () => {
  const renderWithProviders = (props) =>
    render(
      <I18nextProvider i18n={i18n}>
        <BlockchainDashboard {...props} />
      </I18nextProvider>
    );

  it('rend pour chaque rôle et langue', () => {
    ['admin', 'user', 'invité'].forEach(role => {
      ['fr', 'en'].forEach(lang => {
        renderWithProviders({ userRole: role, lang });
        expect(screen.getByRole('region')).toBeInTheDocument();
        expect(screen.getByText(/blockchain/i)).toBeInTheDocument();
      });
    });
  });

  it('affiche le panneau admin uniquement pour admin', () => {
    renderWithProviders({ userRole: 'admin', lang: 'fr' });
    expect(screen.getByRole('button')).toBeInTheDocument();
    renderWithProviders({ userRole: 'user', lang: 'fr' });
    expect(screen.queryByRole('button')).toBeNull();
  });

  it('respecte RGPD (pas de fuite de props sensibles)', () => {
    const { container } = renderWithProviders({ userRole: 'admin', lang: 'fr' });
    expect(container.innerHTML).not.toMatch(/admin/);
  });
});
