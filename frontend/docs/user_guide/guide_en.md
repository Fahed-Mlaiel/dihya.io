# 🛡️ Dihya Coding User Guide

Welcome to Dihya Coding, the first No-Code/Low-Code platform that automatically generates complete digital projects (frontend + backend) from written or voice requirements, with a focus on modern design, security, compliance, and extensibility.

---

## 🚀 What is Dihya Coding?

Dihya Coding is an intelligent platform that allows you to:
- Generate Web Apps (React/Vue/Svelte)
- Generate Mobile Apps (React Native/Flutter)
- Generate APIs (Flask, Node.js, Django)
- Generate AI scripts, DevOps, and Blockchain projects
- Customize UI/UX (Tailwind/Material UI) with Amazigh-inspired themes
- Support multilingual and dialectal content

---

## 🏁 Quick Start

1. **Sign Up & Login**
   - Use the registration/login button at the top
   - Secure authentication via OAuth/JWT
   - Email verification required

2. **Create a New Project**
   - Enter your project description (text or voice)
   - Choose the project type (Web, Mobile, API, etc.)
   - Customize options (design, language, plugins...)

3. **Preview & Generate**
   - Live preview (GitHub Pages/Replit)
   - Download code or share a preview link

---

## 🗺️ Main Features & Routes

| Feature                | Route                    | Description                              | Security/Validation   |
|------------------------|--------------------------|------------------------------------------|-----------------------|
| User Registration      | `/api/auth/register`     | Create a new user account                | Email check, Captcha  |
| Login                  | `/api/auth/login`        | Secure login                             | JWT, Rate Limiting    |
| Project Generation     | `/api/generate`          | Generate a project from requirements     | Role check, Anti-DDoS |
| Project Preview        | `/api/preview`           | Live project preview                     | User check            |
| Plugin Management      | `/api/plugins`           | Add/remove plugins                       | Role check            |
| Auto Translation       | `/api/i18n/translate`    | Translate project automatically          | User check            |
| Send Email             | `/api/mail/send`         | Send email via API                       | Role, Rate Limiting   |
| Download Backup        | `/api/backup/download`   | Download project backup                  | User check            |
| Generation Logs        | `/api/logs/generation`   | View generation logs                     | Admin only            |

---

## 🛡️ Security & Privacy

- **JWT/OAuth** for all sensitive operations
- **Rate Limiting** to prevent abuse
- **Strict CORS** configuration
- **Data encryption** at rest and in transit
- **Audit logs** for all critical actions
- **Full GDPR compliance** (right to erasure, data export, consent)
- **Automatic vulnerability & config audits**

---

## 🌍 Multilingual & Dialect Support

- Automatic support for English, Amazigh, Arabic, French, and dialects
- Dynamic AI-powered translation
- Customizable translations

---

## 🎨 Design & Branding

- Modern, responsive UI
- Themes inspired by Amazigh culture or modern tech
- Customizable colors and logo

---

## ⚙️ Extensibility & Plugins

- Support for Analytics, Stripe, CMS plugins, etc.
- Smart template system by domain (e-commerce, education, social, ...)
- Easy integration of custom plugins

---

## 📜 Compliance & Transparency

- **Open-source project (AGPL)**
- Full documentation of all generation actions (timestamped logs)
- Clear privacy and security policies
- Code provenance verification

---

## 📝 Best Practices

- Validate all user inputs
- Use strong passwords
- Regularly review generation logs
- Keep plugins up to date
- Monitor performance and security from the dashboard

---

## ❓ Support & Help

- [User Guide in English](./guide_en.md)
- [User Guide in Amazigh](./guide_ber.md)
- [User Guide in Arabic](./guide_ar.md)
- [User Guide in French](./guide_fr.md)
- For help: contact@dihya.coding

---

> **Our motto:** From idea to code, in full sovereignty and transparency.
