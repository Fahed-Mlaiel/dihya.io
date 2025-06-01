import { render, screen } from '@testing-library/react';
import { I18nextProvider } from 'react-i18next';
import i18n from '../../../../i18nTestConfig';
import Sante from './index';

jest.mock('../../plugins/SanteAIWidget', () => ({
  SanteAIWidget: jest.fn(() => <div data-testid="sante-ai-widget" />)
}));

describe('Sante métier (ultra avancé)', () => {
  const renderWithProviders = (props) =>
    render(
      <I18nextProvider i18n={i18n}>
        <Sante {...props} />
      </I18nextProvider>
    );

  it('rend pour chaque rôle', () => {
    ['admin', 'user', 'invité'].forEach(role => {
      renderWithProviders({ userRole: role, tenant: 't1' });
      expect(screen.getByRole('region', { name: /santé/i })).toBeInTheDocument();
      expect(screen.getByTestId('sante-ai-widget')).toBeInTheDocument();
      expect(screen.getByText(/gestion santé/i)).toBeInTheDocument();
    });
  });

  it('refuse l\'accès pour un rôle non autorisé', () => {
    renderWithProviders({ userRole: 'hacker', tenant: 't1' });
    expect(screen.queryByRole('region', { name: /santé/i })).toBeNull();
  });

  it('respecte RGPD (pas de fuite de props sensibles)', () => {
    const { container } = renderWithProviders({ userRole: 'admin', tenant: 'secret-tenant' });
    expect(container.innerHTML).not.toMatch(/secret-tenant/);
  });

  it('est accessible (aria-label présent)', () => {
    renderWithProviders({ userRole: 'user', tenant: 't1' });
    expect(screen.getByLabelText(/santé/i)).toBeInTheDocument();
  });

  it('intègre le plugin IA', () => {
    renderWithProviders({ userRole: 'admin', tenant: 't1' });
    expect(screen.getByTestId('sante-ai-widget')).toBeInTheDocument();
  });
});
