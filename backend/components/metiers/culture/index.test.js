import { render } from '@testing-library/react';
import { CultureForm } from './index';

describe('CultureForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<CultureForm lang="fr" />);
    expect(getByLabelText('Culture')).toBeInTheDocument();
  });
});
