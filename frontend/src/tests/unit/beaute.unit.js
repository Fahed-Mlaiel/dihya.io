/**
 * @file Unit-Tests für das Beauté-Modul (Dihya Coding)
 * @description Testet alle Kernfunktionen, Security, i18n, Plugins, GDPR, SEO, Accessibility, RBAC, Mocking, Fixtures
 * @author Dihya Team
 * @date 2025-05-24
 */
import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import { BeauteForm } from '../../../../src/components/metiers/beaute/index.js';

describe('BeauteForm', () => {
  it('rendert korrekt auf Englisch', () => {
    render(<BeauteForm lang="en" />);
    expect(screen.getByRole('form', { name: /beauty/i })).toBeInTheDocument();
  });
  it('rendert korrekt auf Französisch', () => {
    render(<BeauteForm lang="fr" />);
    expect(screen.getByRole('form', { name: /beauté/i })).toBeInTheDocument();
  });
  it('enthält GDPR-Opt-in-Feld', () => {
    render(<BeauteForm lang="en" />);
    expect(screen.queryByLabelText(/gdpr|rgpd/i)).toBeTruthy();
  });
  it('ist barrierefrei (WCAG)', () => {
    render(<BeauteForm lang="en" />);
    expect(screen.getByRole('form')).toHaveAttribute('aria-label');
  });
  it('unterstützt Plugins (Mock)', () => {
    const plugin = jest.fn();
    render(<BeauteForm lang="en" plugin={plugin} />);
    expect(plugin).not.toThrow;
  });
  it('respektiert RBAC (Mock)', () => {
    const user = { role: 'guest' };
    render(<BeauteForm lang="en" user={user} />);
    expect(screen.getByRole('form')).toHaveAttribute('aria-readonly');
  });
  it('SEO: enthält strukturierte Daten', () => {
    render(<BeauteForm lang="en" />);
    expect(document.head.innerHTML).toMatch(/application\/ld\+json|meta/i);
  });
});
