import { render } from '@testing-library/react';
import { ConstructionForm } from './index';

describe('ConstructionForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<ConstructionForm lang="fr" />);
    expect(getByLabelText('Construction')).toBeInTheDocument();
  });
});
