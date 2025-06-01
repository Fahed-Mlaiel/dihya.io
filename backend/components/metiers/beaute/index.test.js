import { render } from '@testing-library/react';
import { BeauteForm } from './index';

describe('BeauteForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<BeauteForm lang="fr" />);
    expect(getByLabelText('Beauté')).toBeInTheDocument();
  });
});
