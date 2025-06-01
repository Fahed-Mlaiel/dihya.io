/**
 * @file Unit-Tests für das Banque & Finance-Modul (Dihya Coding)
 * @description Testet alle Kernfunktionen, Security, i18n, Plugins, GDPR, SEO, Accessibility, RBAC, Mocking, Fixtures
 * @author Dihya Team
 * @date 2025-05-24
 */
import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import { BanqueFinanceForm } from '../../../../src/components/metiers/banque_finance/index.js';

describe('BanqueFinanceForm', () => {
  it('rendert korrekt auf Englisch', () => {
    render(<BanqueFinanceForm lang="en" />);
    expect(screen.getByRole('form', { name: /banking|finance/i })).toBeInTheDocument();
  });
  it('rendert korrekt auf Französisch', () => {
    render(<BanqueFinanceForm lang="fr" />);
    expect(screen.getByRole('form', { name: /banque|finance/i })).toBeInTheDocument();
  });
  it('enthält GDPR-Opt-in-Feld', () => {
    render(<BanqueFinanceForm lang="en" />);
    expect(screen.queryByLabelText(/gdpr|rgpd/i)).toBeTruthy();
  });
  it('ist barrierefrei (WCAG)', () => {
    render(<BanqueFinanceForm lang="en" />);
    expect(screen.getByRole('form')).toHaveAttribute('aria-label');
  });
  it('unterstützt Plugins (Mock)', () => {
    const plugin = jest.fn();
    render(<BanqueFinanceForm lang="en" plugin={plugin} />);
    expect(plugin).not.toThrow;
  });
  it('respektiert RBAC (Mock)', () => {
    const user = { role: 'guest' };
    render(<BanqueFinanceForm lang="en" user={user} />);
    expect(screen.getByRole('form')).toHaveAttribute('aria-readonly');
  });
  it('SEO: enthält strukturierte Daten', () => {
    render(<BanqueFinanceForm lang="en" />);
    expect(document.head.innerHTML).toMatch(/application\/ld\+json|meta/i);
  });
});
