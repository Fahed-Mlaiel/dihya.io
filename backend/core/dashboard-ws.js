// dashboard-ws.js
// WebSocket temps réel pour dashboard global Dihya (Node.js/Express + ws)
// Diffuse le dashboard Markdown, logs temps réel, alertes personnalisées

const fs = require('fs');
const path = require('path');
const http = require('http');
const express = require('express');
const WebSocket = require('ws');

const DASHBOARD_MD_PATH = path.join(__dirname, '../../dashboard_global.md');
const PORT = process.env.DASHBOARD_WS_PORT || 8081;

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server, path: '/ws/dashboard' });

function readDashboardMd() {
  try {
    return fs.readFileSync(DASHBOARD_MD_PATH, 'utf-8');
  } catch (e) {
    return `Erreur lecture dashboard: ${e}`;
  }
}

// Multi-tenant : mapping clients <-> tenant
const clientTenants = new Map();

wss.on('connection', (ws, req) => {
  // Extraction du tenant (query string ?tenant=... ou header)
  let tenant = 'default';
  try {
    const url = new URL(req.url, 'ws://localhost');
    tenant = url.searchParams.get('tenant') || req.headers['x-tenant'] || 'default';
  } catch {}
  clientTenants.set(ws, tenant);
  ws.send(JSON.stringify({ type: 'dashboard', tenant, data: readDashboardMd() }));
  ws.on('message', (msg) => {
    if (msg === 'refresh') ws.send(JSON.stringify({ type: 'dashboard', tenant, data: readDashboardMd() }));
    if (msg.startsWith('alert:')) ws.send(JSON.stringify({ type: 'alert', tenant, data: msg.slice(6) }));
    if (msg.startsWith('setWidget:')) {
      // Personnalisation widget métier par tenant
      try {
        const { widget, value } = JSON.parse(msg.slice(10));
        if (!global.widgets) global.widgets = {};
        if (!global.widgets[tenant]) global.widgets[tenant] = {};
        global.widgets[tenant][widget] = value;
        ws.send(JSON.stringify({ type: 'widget', tenant, widget, value }));
      } catch {}
    }
  });
  ws.on('close', () => clientTenants.delete(ws));
});

// Diffusion ciblée par tenant
function broadcastToTenant(tenant, payload) {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN && clientTenants.get(client) === tenant) {
      client.send(JSON.stringify(payload));
    }
  });
}

// Alerte automatique : seuil SLA ou incident critique
function checkSLAAndAlert(tenant = 'default') {
  const sla = getSLA();
  if (sla.sla < 99.0) {
    broadcastToTenant(tenant, { type: 'alert', tenant, data: `SLA bas (${sla.sla}%)` });
  }
  if (sla.lastIncident && sla.lastIncident.severity === 'critical') {
    broadcastToTenant(tenant, { type: 'alert', tenant, data: `Incident critique : ${sla.lastIncident.message}` });
  }
}

// Widget métier personnalisé par tenant (exemple mock)
function setTenantWidget(tenant, widget, value) {
  if (!global.widgets) global.widgets = {};
  if (!global.widgets[tenant]) global.widgets[tenant] = {};
  global.widgets[tenant][widget] = value;
  broadcastToTenant(tenant, { type: 'widget', tenant, widget, value });
}

// Extension : logs temps réel (exemple)
function broadcastLog(log) {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(`[LOG] ${log}`);
    }
  });
}

// Extension : push d’alerte personnalisée
function broadcastAlert(message) {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(`[ALERTE] ${message}`);
    }
  });
}

// Extension : gestion des incidents live
let incidents = [];
let slaStats = { total: 0, incidents: 0, lastIncident: null };

function broadcastIncident(incident) {
  incidents.push({ ...incident, timestamp: new Date().toISOString() });
  slaStats.incidents++;
  slaStats.lastIncident = incident;
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send('[INCIDENT] ' + JSON.stringify(incident));
    }
  });
}

function getSLA() {
  const total = Math.max(slaStats.total, 1);
  const sla = ((total - slaStats.incidents) / total) * 100;
  return { sla: sla.toFixed(2), total, incidents: slaStats.incidents, lastIncident: slaStats.lastIncident };
}

// Widget métier : nombre d'utilisateurs actifs (exemple mock)
let activeUsers = 0;
function setActiveUsers(n) {
  activeUsers = n;
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send('[WIDGET] {"activeUsers":' + activeUsers + '}');
    }
  });
}

// Exemple : push log/alerte depuis la CLI ou un script
if (require.main === module) {
  server.listen(PORT, () => {
    console.log(`Dashboard WebSocket server running on ws://localhost:${PORT}/ws/dashboard`);
  });
  // Pour test manuel :
  // setInterval(() => broadcastLog('Ping temps réel ' + new Date().toISOString()), 15000);
  // setTimeout(() => broadcastAlert('Incident critique détecté !'), 30000);
  // setInterval(() => { slaStats.total++; }, 60000); // Simule uptime
  // setTimeout(() => broadcastIncident({ type: 'DB', message: 'Incident DB critique', severity: 'critical' }), 20000);
  // setInterval(() => setActiveUsers(Math.floor(Math.random()*100)), 10000);
}

module.exports = { server, broadcastLog, broadcastAlert, broadcastIncident, getSLA, setActiveUsers, setTenantWidget, checkSLAAndAlert };
