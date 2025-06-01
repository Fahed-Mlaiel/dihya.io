import { render, screen } from '@testing-library/react';
import { Automobile } from './index';

describe('Automobile métier (ultra avancé)', () => {
  const pluginMock = { render: () => <div data-testid="plugin-mock">Plugin</div> };

  it('rend pour chaque rôle et langue', () => {
    ['admin', 'user', 'invité'].forEach(role => {
      ['fr', 'en'].forEach(lang => {
        render(<Automobile userRole={role} lang={lang} plugin={pluginMock} />);
        expect(screen.getByRole('region', { name: /automobile|automotive/i })).toBeInTheDocument();
        expect(screen.getByTestId('plugin-mock')).toBeInTheDocument();
      });
    });
  });

  it('respecte RGPD (pas de fuite de props sensibles)', () => {
    const { container } = render(<Automobile userRole="admin" lang="fr" plugin={pluginMock} />);
    expect(container.innerHTML).not.toMatch(/admin/);
  });

  it('est accessible (aria-label présent)', () => {
    render(<Automobile userRole="user" lang="fr" />);
    expect(screen.getByLabelText(/automobile/i)).toBeInTheDocument();
  });

  it('intègre le plugin métier', () => {
    render(<Automobile userRole="user" lang="fr" plugin={pluginMock} />);
    expect(screen.getByTestId('plugin-mock')).toBeInTheDocument();
  });
});
