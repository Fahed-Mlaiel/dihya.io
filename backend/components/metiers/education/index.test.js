import { render } from '@testing-library/react';
import { EducationForm } from './index';

describe('EducationForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<EducationForm lang="fr" />);
    expect(getByLabelText('Éducation')).toBeInTheDocument();
  });
});
