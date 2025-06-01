import { render } from '@testing-library/react';
import { AutomobileForm } from './index';

describe('AutomobileForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<AutomobileForm lang="fr" />);
    expect(getByLabelText('Automobile')).toBeInTheDocument();
  });
});
