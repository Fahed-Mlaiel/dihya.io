import { render } from '@testing-library/react';
import { CryptoForm } from './index';

describe('CryptoForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<CryptoForm lang="fr" />);
    expect(getByLabelText('Crypto')).toBeInTheDocument();
  });
});
