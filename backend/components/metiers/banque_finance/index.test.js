import { render } from '@testing-library/react';
import { BanqueFinanceForm } from './index';

describe('BanqueFinanceForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<BanqueFinanceForm lang="fr" />);
    expect(getByLabelText('Banque & Finance')).toBeInTheDocument();
  });
});
