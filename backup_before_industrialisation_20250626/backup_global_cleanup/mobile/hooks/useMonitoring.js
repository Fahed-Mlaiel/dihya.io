// Hook métier pour le monitoring (statistiques, alertes, santé système)
import { useState, useEffect } from 'react';

export function useMonitoring() {
  const [stats, setStats] = useState({ users: 0, actions: 0, errors: 0 });
  const [alerts, setAlerts] = useState([]);
  const [health, setHealth] = useState('unknown');

  useEffect(() => {
    // Simulation d’un fetch vers une API de monitoring
    fetch('/api/monitoring/health')
      .then(r => r.json())
      .then(data => {
        setStats(data.stats);
        setAlerts(data.alerts);
        setHealth(data.health);
      })
      .catch(() => setHealth('degraded'));
  }, []);

  const addAlert = (alert) => setAlerts(a => [...a, alert]);

  return { stats, alerts, health, addAlert };
}
