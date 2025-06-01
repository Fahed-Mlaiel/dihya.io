import { render } from '@testing-library/react';
import AssuranceForm from './index';

describe('AssuranceForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<AssuranceForm lang="fr" />);
    expect(getByLabelText('Assurance')).toBeInTheDocument();
  });
});
