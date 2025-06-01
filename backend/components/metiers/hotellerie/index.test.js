import { render } from '@testing-library/react';
import { HotellerieForm } from './index';

describe('HotellerieForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<HotellerieForm lang="fr" />);
    expect(getByLabelText('Hôtellerie')).toBeInTheDocument();
  });
});
