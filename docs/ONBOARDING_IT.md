# Guida Onboarding Dihya Coding (IT)

## Introduzione
Dihya Coding è una piattaforma open source per la gestione e lo sviluppo di progetti IA, VR, AR, web e mobile, con sicurezza avanzata, internazionalizzazione dinamica, estendibilità e piena conformità agli standard globali (GDPR, audit, SEO, accessibilità).

## Avvio rapido
1. **Clona il repository:**
   ```bash
   git clone https://github.com/dihya-coding/dihya.git
   ```
2. **Configura l'ambiente:**
   - Assicurati di avere Python 3.10+, Node.js 18+ e Docker.
   - Installa le dipendenze:
     ```bash
     pip install -r requirements.txt
     npm install
     ```
3. **Avvia l'applicazione:**
   ```bash
   make dev
   ```
4. **Accedi:**
   - Usa l'account guest o registrati tramite l'interfaccia web.

## Sicurezza e conformità
- Tutto il traffico è cifrato (HTTPS).
- Autenticazione JWT, CORS, WAF, anti-DDOS.
- Conformità GDPR, log di audit, esportazione dati.

## Internazionalizzazione
- Supporta: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Contributo e supporto
- Consulta `CONTRIBUTING_IT.md`.
- Apri issue su [GitHub Issues](https://github.com/dihya-coding/dihya/issues).

## Esempio: Crea un nuovo progetto IA
```bash
curl -X POST /api/projects -H 'Authorization: Bearer <token>' -d '{"type": "ia"}'
```

## Link chiave
- [Guida sicurezza](./securite_GUIDE_IT.md)
- [Roadmap](./ROADMAP_EN.md)
- [Documentazione completa](./README_IT.md)

---
© 2025 Dihya Coding. Tutti i diritti riservati.
