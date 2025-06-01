# Template Métier : Beauté

## Présentation

Ce template métier permet de générer un backend d’application pour le secteur **Beauté** : gestion de salons, rendez-vous, prestations, clients, paiements, notifications, etc.  
Pensé pour la plateforme **Dihya Coding** : extensible, sécurisé, multilingue, prêt à l’emploi.

---

## Fonctionnalités principales

- **Gestion des salons et instituts** (création, planning, équipe)
- **Gestion des prestations** (catalogue, tarifs, durée, disponibilité)
- **Prise de rendez-vous en ligne** (création, modification, annulation)
- **Gestion des clients** (profil, historique, fidélité)
- **Paiement et facturation** (historique, relances)
- **Notifications automatiques** (email, SMS, tableau de bord)
- **Export des rendez-vous et clients (CSV/PDF)**
- **API ouverte** pour intégration (paiement, CRM, partenaires)
- **Multilingue** (français, amazigh, dialectes)

---

## Structure des routes (exemples)

| Méthode | Endpoint                     | Description                        | Authentification |
|---------|------------------------------|------------------------------------|------------------|
| GET     | `/api/salons`                | Liste des salons                   | Admin/User       |
| POST    | `/api/salons`                | Créer un salon                     | Admin            |
| GET     | `/api/prestations`           | Liste des prestations              | Public           |
| POST    | `/api/prestations`           | Ajouter une prestation             | Admin            |
| GET     | `/api/rendezvous`            | Liste des rendez-vous              | Salon/Client     |
| POST    | `/api/rendezvous`            | Prendre rendez-vous                | Client           |
| GET     | `/api/clients`               | Liste des clients                  | Admin/Salon      |
| POST    | `/api/clients`               | Créer un client                    | Salon            |
| GET     | `/api/export/rendezvous`     | Exporter rendez-vous (CSV/PDF)     | Admin            |

---

## Modèles de données (extraits)

- **Salon** : id, nom, adresse, équipe, prestations, planning
- **Prestation** : id, nom, tarif, durée, description, disponibilité
- **Rendez-vous** : id, client, salon, prestation, date, statut
- **Client** : id, nom, email, historique, fidélité
- **Notification** : id, client, type, message, date

---

## Sécurité & RGPD

- Authentification JWT/OAuth2
- Permissions par rôle (Admin, Salon, Client, Invité)
- Logs horodatés (audit)
- Export/suppression des données sur demande (RGPD)
- Protection CORS, rate limiting, anti-DDoS

---

## Extensibilité

- Ajoutez vos propres routes dans `template.py`
- Branchez des plugins (paiement, CRM, analytics)
- Compatible marketplace Dihya (import/export)

---

## Design & UX

- **UI/UX** : Moderne, épuré, inspiration bien-être (voir frontend)
- **Responsive** : Adapté mobile/tablette
- **Accessibilité** : ARIA, contrastes, navigation clavier

---

## Exemple de logique métier (pseudo-code)

```python
# Prise de rendez-vous
@app.route('/api/rendezvous', methods=['POST'])
@jwt_required()
def prendre_rendezvous():
    data = request.get_json()
    # Validation, création, notification, log...
    return jsonify({"message": "Rendez-vous pris"}), 201