// Hook métier pour la gestion des logs d’accès et d’audit
import { useState } from 'react';

export function useLogs() {
  const [logs, setLogs] = useState([]);

  const addLog = (action, user) => {
    const entry = { action, user, date: new Date().toISOString() };
    setLogs(l => [...l, entry]);
    // Optionnel : envoyer vers un endpoint d’auditabilité
  };

  const clearLogs = () => setLogs([]);

  return { logs, addLog, clearLogs };
}
