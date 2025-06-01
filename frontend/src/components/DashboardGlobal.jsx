import { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';

/**
 * DashboardGlobal – Affichage visuel avancé du dashboard global conformité/monitoring Dihya
 * - Affiche le Markdown, les badges SVG, les indicateurs dynamiques, les graphiques Mermaid
 * - Rafraîchissement automatique, accessibilité, i18n-ready
 */
const DASHBOARD_MD_URL = '/Dihya/backend/dashboard_global.md';
const BADGE_DB_URL = '/Dihya/backend/db/tests/coverage_db_badge.svg';
const BADGE_CONFORMITE_URL = '/Dihya/backend/compliance/reports/badge_conformite.svg';

export default function DashboardGlobal() {
  const [markdown, setMarkdown] = useState('');
  const [lastUpdate, setLastUpdate] = useState(Date.now());
  const [isLive, setIsLive] = useState(false);
  const [logs, setLogs] = useState([]);
  const [alerts, setAlerts] = useState([]);
  const [incidents, setIncidents] = useState([]);
  const [sla, setSla] = useState({ sla: '100.00', total: 0, incidents: 0, lastIncident: null });
  const [activeUsers, setActiveUsers] = useState(0);
  const [tenant, setTenant] = useState('default');
  const [tenantWidgets, setTenantWidgets] = useState({});

  // Polling régulier (30s)
  useEffect(() => {
    let active = true;
    function fetchDashboard() {
      fetch(DASHBOARD_MD_URL)
        .then(res => res.text())
        .then(md => { if (active) { setMarkdown(md); setLastUpdate(Date.now()); } });
    }
    fetchDashboard();
    const interval = setInterval(fetchDashboard, 30000);
    return () => { active = false; clearInterval(interval); };
  }, []);

  // WebSocket (optionnel, si backend disponible)
  useEffect(() => {
    let ws;
    if (window.WebSocket) {
      const wsUrl = `ws://${window.location.hostname}:8081/ws/dashboard?tenant=${tenant}`;
      ws = new window.WebSocket(wsUrl);
      ws.onopen = () => setIsLive(true);
      ws.onmessage = (event) => {
        let data;
        try { data = JSON.parse(event.data); } catch { data = event.data; }
        if (typeof data === 'string') setMarkdown(data);
        else if (data.type === 'dashboard') setMarkdown(data.data);
        else if (data.type === 'log') setLogs(l => [...l.slice(-19), data.data]);
        else if (data.type === 'alert') setAlerts(a => [...a.slice(-9), data.data]);
        else if (data.type === 'incident') setIncidents(i => [...i.slice(-9), data.data]);
        else if (data.type === 'widget') setTenantWidgets(w => ({ ...w, [data.widget]: data.value }));
      };
      ws.onclose = () => setIsLive(false);
    }
    return () => { if (ws) ws.close(); };
  }, [tenant]);

  // Widget SLA (calcul local, peut être mis à jour par le backend)
  useEffect(() => {
    setSla(s => ({ ...s, sla: (s.total ? ((s.total - s.incidents) / s.total * 100).toFixed(2) : '100.00') }));
  }, [incidents]);

  return (
    <div className="dashboard-global">
      <h2>Dashboard Global Conformité & Monitoring</h2>
      <div style={{ fontSize: 12, color: '#888', marginBottom: 8 }}>
        {isLive ? '🔴 Temps réel (WebSocket)' : `⏳ Dernier rafraîchissement : ${new Date(lastUpdate).toLocaleTimeString()}`}
      </div>
      <div className="badges" style={{ display: 'flex', gap: 24, marginBottom: 24 }}>
        <div>
          <img src={BADGE_CONFORMITE_URL} alt="Badge conformité backend" height={40} />
          <div>Conformité backend/core</div>
        </div>
        <div>
          <img src={BADGE_DB_URL} alt="Badge couverture DB" height={40} />
          <div>Couverture tests DB</div>
        </div>
      </div>
      <div className="dashboard-markdown" style={{ background: '#fff', borderRadius: 8, padding: 24, boxShadow: '0 2px 8px #0001' }}>
        <MarkdownRenderer markdown={markdown} />
      </div>
      <iframe
        title="Dashboard Markdown"
        src={DASHBOARD_MD_URL.replace('.md', '.html')}
        style={{ width: '100%', height: 600, border: 'none', marginTop: 32 }}
      />
      <div className="dashboard-widgets" style={{ marginTop: 32 }}>
        <h3>Logs temps réel</h3>
        <ul style={{ fontSize: 13, background: '#f8f8f8', borderRadius: 6, padding: 12, minHeight: 40 }}>
          {logs.map((log, i) => <li key={i}>{log}</li>)}
        </ul>
        <h3>Alertes live</h3>
        <ul style={{ fontSize: 14, color: '#b00', background: '#fff6f6', borderRadius: 6, padding: 12, minHeight: 40 }}>
          {alerts.map((alert, i) => <li key={i}>{alert}</li>)}
        </ul>
        <h3>Incidents live</h3>
        <ul style={{ fontSize: 14, color: '#b00', background: '#fff6f6', borderRadius: 6, padding: 12, minHeight: 40 }}>
          {incidents.map((inc, i) => <li key={i}>{inc.timestamp} [{inc.severity}] {inc.type} : {inc.message}</li>)}
        </ul>
        <h3>SLA (Service Level Agreement)</h3>
        <div style={{ fontSize: 15, color: '#0a0', background: '#f6fff6', borderRadius: 6, padding: 12, minHeight: 40 }}>
          SLA actuel : <b>{sla.sla}%</b> (incidents : {incidents.length})
        </div>
        <h3>Widget métier : utilisateurs actifs</h3>
        <div style={{ fontSize: 15, color: '#005', background: '#f0f4ff', borderRadius: 6, padding: 12, minHeight: 40 }}>
          Utilisateurs actifs (live) : <b>{activeUsers}</b>
        </div>
        <div style={{ margin: '16px 0' }}>
          <label>Tenant : </label>
          <input value={tenant} onChange={e => setTenant(e.target.value)} style={{ width: 120, marginLeft: 8 }} />
        </div>
        <h3>Widgets personnalisés (tenant)</h3>
        <ul style={{ fontSize: 15, color: '#005', background: '#f0f4ff', borderRadius: 6, padding: 12, minHeight: 40 }}>
          {Object.entries(tenantWidgets).map(([k, v]) => <li key={k}>{k} : <b>{v}</b></li>)}
        </ul>
      </div>
    </div>
  );
}

// Composant de rendu Markdown (simple, peut être remplacé par react-markdown ou autre)
function MarkdownRenderer({ markdown }) {
  if (typeof ReactMarkdown !== 'undefined') {
    return <ReactMarkdown>{markdown}</ReactMarkdown>;
  }
  return <pre style={{ whiteSpace: 'pre-wrap', fontFamily: 'inherit' }}>{markdown}</pre>;
}
