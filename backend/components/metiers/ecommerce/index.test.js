import { render } from '@testing-library/react';
import { EcommerceForm } from './index';

describe('EcommerceForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<EcommerceForm lang="fr" />);
    expect(getByLabelText('E-Commerce')).toBeInTheDocument();
  });
});
