import { render } from '@testing-library/react';
import { EnergieForm } from './index';

describe('EnergieForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<EnergieForm lang="fr" />);
    expect(getByLabelText('Énergie')).toBeInTheDocument();
  });
});
