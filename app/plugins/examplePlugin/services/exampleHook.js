// Exemple de hook React pour le plugin

import { useState } from 'react';

export function usePluginToggle(initial = false) {
  const [enabled, setEnabled] = useState(initial);
  const toggle = () => setEnabled(e => !e);
  return [enabled, toggle];
}
