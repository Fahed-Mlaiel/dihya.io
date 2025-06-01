# Guide des webhooks Dihya

- Intégration de webhooks (événements, notifications, CI/CD, plugins)
- Sécurité, authentification, validation, logs
- Exemples d’implémentation (backend, frontend, cloud)
- Tests, monitoring, alertes

Voir [API_REFERENCE_FR.md](docs/API_REFERENCE_FR.md), [MONITORING_GUIDE.md](MONITORING_GUIDE.md)

# 🔗 Dihya – Webhooks Guide Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Introduction](#introduction)
- [Qu’est-ce qu’un webhook ?](#quest-ce-quun-webhook)
- [Architecture & sécurité des webhooks](#architecture--sécurité-des-webhooks)
- [Configuration d’un webhook Dihya](#configuration-dun-webhook-dihya)
- [Exemples multi-stack](#exemples-multi-stack)
  - [Exemple Flask (Python)](#exemple-flask-python)
  - [Exemple Node.js (Express)](#exemple-nodejs-express)
  - [Exemple Django](#exemple-django)
  - [Exemple Frontend (React)](#exemple-frontend-react)
- [Tests & monitoring](#tests--monitoring)
- [Templates & bonnes pratiques](#templates--bonnes-pratiques)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce guide explique comment utiliser, sécuriser, tester et monitorer les webhooks dans **Dihya**.
Il couvre la configuration multi-stack (Flask, Node, Django, React…), la sécurité (signature, replay, RBAC), la souveraineté (aucune dépendance propriétaire), l’accessibilité et la documentation multilingue (fr, en, ar, tzm).

---

## Qu’est-ce qu’un webhook ?

Un webhook est un mécanisme permettant à Dihya de notifier un système externe lorsqu’un événement se produit (création de template, validation, incident sécurité, etc.).
Les webhooks sont essentiels pour l’intégration continue, l’automatisation, la traçabilité et la souveraineté numérique.

---

## Architecture & sécurité des webhooks

- **Signature HMAC SHA-256** (clé secrète configurable, rotation possible)
- **Replay protection** (horodatage, nonce, TTL)
- **Payload JSON structuré, multilingue**
- **RBAC** : seuls les rôles autorisés peuvent créer/modifier des webhooks
- **Logs & audit** : chaque appel est journalisé, exportable, RGPD-ready
- **Fallback open source** : aucun appel externe obligatoire, tout est documenté

---

## Configuration d’un webhook Dihya

1. **Créer un endpoint HTTP(S)** sur votre système (voir exemples ci-dessous)
2. **Configurer le webhook dans Dihya** (UI ou API)
   - URL cible
   - Secret partagé (pour signature HMAC)
   - Événements à écouter (ex : `template.created`, `incident.security`)
   - Format du payload (JSON, multilingue)
3. **Tester le webhook** via l’UI ou la CLI Dihya
4. **Vérifier la signature et la validité du payload côté récepteur**

---

## Exemples multi-stack

### Exemple Flask (Python)

```python
from flask import Flask, request, abort
import hmac, hashlib, json

app = Flask(__name__)
WEBHOOK_SECRET = b"votre_secret_webhook"

def verify_signature(payload, signature):
    mac = hmac.new(WEBHOOK_SECRET, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(mac, signature)

@app.route("/webhook/dihya", methods=["POST"])
def webhook():
    signature = request.headers.get("X-Dihya-Signature", "")
    if not verify_signature(request.data, signature):
        abort(403)
    data = json.loads(request.data)
    # Traitez l’événement ici
    return "OK", 200
```

### Exemple Node.js (Express)

```js
const express = require("express");
const crypto = require("crypto");
const app = express();
app.use(express.json({ verify: (req, res, buf) => { req.rawBody = buf; } }));

const WEBHOOK_SECRET = "votre_secret_webhook";

function verifySignature(payload, signature) {
  const hmac = crypto.createHmac("sha256", WEBHOOK_SECRET);
  hmac.update(payload);
  return hmac.digest("hex") === signature;
}

app.post("/webhook/dihya", (req, res) => {
  const signature = req.headers["x-dihya-signature"];
  if (!verifySignature(req.rawBody, signature)) return res.sendStatus(403);
  // Traitez l’événement ici
  res.send("OK");
});
```

### Exemple Django

```python
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseForbidden
import hmac, hashlib, json

WEBHOOK_SECRET = b"votre_secret_webhook"

@csrf_exempt
def dihyawh(request):
    if request.method != "POST":
        return HttpResponseForbidden()
    signature = request.headers.get("X-Dihya-Signature", "")
    mac = hmac.new(WEBHOOK_SECRET, request.body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(mac, signature):
        return HttpResponseForbidden()
    data = json.loads(request.body)
    # Traitez l’événement ici
    return HttpResponse("OK")
```

### Exemple Frontend (React)

> ⚠️ Pour des raisons de sécurité, ne recevez jamais de webhook directement côté frontend. Utilisez un backend intermédiaire.

---

## Tests & monitoring

- **Tests unitaires** : vérification signature, payload, replay
- **Tests d’intégration** : simulation d’événements, monitoring Prometheus/Grafana
- **Logs** : chaque appel, succès/échec, horodaté, exportable
- **Audit** : conformité RGPD/NIS2, accessibilité, souveraineté

---

## Templates & bonnes pratiques

### Template de payload webhook

```json
{
  "event": "template.created",
  "timestamp": "2025-05-20T12:00:00Z",
  "lang": "fr",
  "data": {
    "template_id": "abc123",
    "user_id": "user42",
    "details": {
      "fr": "Nouveau template créé",
      "en": "New template created",
      "ar": "تم إنشاء قالب جديد",
      "tzm": "Yettwarna template amaynut"
    }
  }
}
```

### Bonnes pratiques

- Toujours vérifier la signature côté récepteur
- Limiter les IP sources (firewall, allowlist)
- Logger chaque appel, succès/échec
- Documenter chaque endpoint webhook (OpenAPI, doc multilingue)
- Tester chaque scénario (succès, échec, replay, payload corrompu)
- Ne jamais exposer de secret dans le payload

---

## Multilingue

- **Français** : Ce guide est disponible en français.
- **English** : This guide is available in English.
- **العربية** : هذا الدليل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-webhooks
- **Email** : webhooks@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/votre-org/dihya/issues)

---

> **Ce guide est validé pour la production. Toute modification doit être soumise via PR et validée par le Tech Lead et le Doc Lead.**
