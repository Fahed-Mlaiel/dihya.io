import { render, screen } from '@testing-library/react';
import { Assurance } from './index';

describe('Assurance métier (ultra avancé)', () => {
  const pluginMock = { render: () => <div data-testid="plugin-mock">Plugin</div> };

  it('rend pour chaque rôle et langue', () => {
    ['admin', 'user', 'invité'].forEach(role => {
      ['fr', 'en'].forEach(lang => {
        render(<Assurance userRole={role} lang={lang} plugin={pluginMock} />);
        expect(screen.getByRole('region', { name: /assurance|insurance/i })).toBeInTheDocument();
        expect(screen.getByTestId('plugin-mock')).toBeInTheDocument();
      });
    });
  });

  it('respecte RGPD (pas de fuite de props sensibles)', () => {
    const { container } = render(<Assurance userRole="admin" lang="fr" plugin={pluginMock} />);
    expect(container.innerHTML).not.toMatch(/admin/);
  });

  it('est accessible (aria-label présent)', () => {
    render(<Assurance userRole="user" lang="fr" />);
    expect(screen.getByLabelText(/assurance/i)).toBeInTheDocument();
  });

  it('intègre le plugin métier', () => {
    render(<Assurance userRole="user" lang="fr" plugin={pluginMock} />);
    expect(screen.getByTestId('plugin-mock')).toBeInTheDocument();
  });
});
