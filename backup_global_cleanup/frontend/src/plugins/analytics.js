// Plugin Analytics avancé : tracking RGPD, multi-event, export CSV
export function trackEvent(event, data, userId) {
  if (!event) throw new Error('Event requis');
  fetch('https://analytics.dihya.io/track', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ event, data, userId, timestamp: Date.now() })
  });
}
export function exportAnalyticsCSV(events) {
  const header = 'event,data,userId,timestamp\n';
  const rows = events.map(e => [e.event, JSON.stringify(e.data), e.userId, e.timestamp].join(',')).join('\n');
  return header + rows;
}
