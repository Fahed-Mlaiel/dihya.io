import { render } from '@testing-library/react';
import { BtpForm } from './index';

describe('BtpForm', () => {
  it('rendert ohne Fehler', () => {
    const { getByLabelText } = render(<BtpForm lang="fr" />);
    expect(getByLabelText('BTP')).toBeInTheDocument();
  });
});
