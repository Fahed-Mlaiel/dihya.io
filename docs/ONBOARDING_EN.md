# Dihya Coding Onboarding Guide (EN)

## Introduction
Dihya Coding is an open-source platform for managing and developing AI, VR, AR, web, and mobile projects, with advanced security, dynamic internationalization, extensibility, and full compliance with global standards (GDPR, audit, SEO, accessibility).

## Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/dihya-coding/dihya.git
   ```
2. **Setup environment:**
   - Ensure Python 3.10+, Node.js 18+, and Docker are installed.
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     npm install
     ```
3. **Run the app:**
   ```bash
   make dev
   ```
4. **Login:**
   - Use the guest account or register via the web UI.

## Security & Compliance
- All traffic is encrypted (HTTPS).
- JWT authentication, CORS, WAF, anti-DDOS.
- Full GDPR compliance, audit logs, exportable data.

## Internationalization
- Supports: fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es.

## Contribution & Support
- See `CONTRIBUTING_EN.md`.
- Open issues at [GitHub Issues](https://github.com/dihya-coding/dihya/issues).

## Example: Create a new AI project
```bash
curl -X POST /api/projects -H 'Authorization: Bearer <token>' -d '{"type": "ai"}'
```

## Key Links
- [Security Guide](./securite_GUIDE_EN.md)
- [Roadmap](./ROADMAP_EN.md)
- [Full Documentation](./README_EN.md)

---
© 2025 Dihya Coding. All rights reserved.
