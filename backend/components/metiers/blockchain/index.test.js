import { render } from '@testing-library/react';
import { BlockchainForm } from './index';

describe('BlockchainForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<BlockchainForm lang="fr" />);
    expect(getByLabelText('Blockchain')).toBeInTheDocument();
  });
});
