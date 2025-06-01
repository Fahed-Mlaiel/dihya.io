# Template Métier : BTP (Bâtiment & Travaux Publics)

## Présentation

Ce template métier permet de générer un backend d’application pour le secteur **BTP** : gestion de chantiers, projets, équipes, matériels, fournisseurs, plannings, suivi financier, etc.  
Pensé pour la plateforme **Dihya Coding** : extensible, sécurisé, multilingue, prêt à l’emploi.

---

## Fonctionnalités principales

- **Gestion des chantiers et projets** (création, suivi, historique)
- **Gestion des équipes et ouvriers** (affectation, planning, sécurité)
- **Gestion du matériel et des stocks** (entrée/sortie, maintenance)
- **Gestion des fournisseurs et sous-traitants**
- **Suivi financier** (budgets, dépenses, factures)
- **Gestion documentaire** (plans, permis, rapports, photos)
- **Notifications et alertes** (retards, incidents, échéances)
- **Export des données (CSV/PDF)**
- **API ouverte** pour intégration (ERP, IoT, partenaires)
- **Multilingue** (français, amazigh, dialectes)

---

## Structure des routes (exemples)

| Méthode | Endpoint                     | Description                        | Authentification |
|---------|------------------------------|------------------------------------|------------------|
| GET     | `/api/chantiers`             | Liste des chantiers                | Admin/User       |
| POST    | `/api/chantiers`             | Créer un chantier                  | Admin            |
| GET     | `/api/equipes`               | Liste des équipes                  | Admin/User       |
| POST    | `/api/equipes`               | Créer une équipe                   | Admin            |
| GET     | `/api/materiels`             | Liste du matériel                  | Admin/User       |
| POST    | `/api/materiels`             | Ajouter du matériel                | Admin            |
| GET     | `/api/fournisseurs`          | Liste des fournisseurs             | Admin            |
| POST    | `/api/fournisseurs`          | Ajouter un fournisseur             | Admin            |
| GET     | `/api/finances`              | Suivi financier                    | Admin            |
| GET     | `/api/export/chantiers`      | Exporter chantiers (CSV/PDF)       | Admin            |

---

## Modèles de données (extraits)

- **Chantier** : id, nom, localisation, début/fin, statut, équipes, budget, documents
- **Équipe** : id, nom, membres, chef, chantiers
- **Matériel** : id, nom, type, état, disponibilité, historique
- **Fournisseur** : id, nom, contact, spécialité, contrats
- **Finance** : id, chantier, budget, dépenses, factures, statut

---

## Sécurité & RGPD

- Authentification JWT/OAuth2
- Permissions par rôle (Admin, Chef de chantier, Ouvrier, Invité)
- Logs horodatés (audit)
- Export/suppression des données sur demande (RGPD)
- Protection CORS, rate limiting, anti-DDoS

---

## Extensibilité

- Ajoutez vos propres routes dans `template.py`
- Branchez des plugins (ERP, IoT, analytics)
- Compatible marketplace Dihya (import/export)

---

## Design & UX

- **UI/UX** : Moderne, épuré, inspiration chantier (voir frontend)
- **Responsive** : Adapté mobile/tablette
- **Accessibilité** : ARIA, contrastes, navigation clavier

---

## Exemple de logique métier (pseudo-code)

```python
# Création d’un chantier
@app.route('/api/chantiers', methods=['POST'])
@jwt_required()
def creer_chantier():
    data = request.get_json()
    # Validation, création, log...
    return jsonify({"message": "Chantier créé"}), 201