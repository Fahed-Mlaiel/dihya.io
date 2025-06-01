import { render, screen } from '@testing-library/react';
import App from '../../App';

test('affiche le texte de bienvenue', () => {
  render(<App />);
  expect(screen.getByText(/Hello, Dihya Frontend!/i)).toBeInTheDocument();
});
