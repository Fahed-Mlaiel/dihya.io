"""
Client Stripe pour la gestion des paiements – Dihya Coding

Ce module encapsule les appels à l’API Stripe pour garantir la sécurité,
la validation des données et la traçabilité des transactions.

Bonnes pratiques :
- Ne jamais stocker la clé API en dur (utiliser les variables d’environnement)
- Logger chaque opération pour auditabilité
- Gérer les erreurs et les timeouts de façon robuste
- Valider les données avant chaque appel API
"""

import os
import logging
from typing import Optional, Dict, Any

import stripe

STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
stripe.api_key = STRIPE_API_KEY

logger = logging.getLogger("dihya.api_clients.stripe")
logger.setLevel(logging.INFO)

def create_payment_intent(
    amount: int,
    currency: str = "eur",
    metadata: Optional[Dict[str, Any]] = None,
    description: Optional[str] = None
) -> Optional[str]:
    """
    Crée un PaymentIntent Stripe pour un paiement sécurisé.

    Args:
        amount (int): Montant en centimes (ex: 1000 pour 10,00€).
        currency (str): Devise (par défaut 'eur').
        metadata (dict, optional): Métadonnées personnalisées.
        description (str, optional): Description du paiement.

    Returns:
        str: ID du PaymentIntent si succès, None sinon.

    Raises:
        ValueError: Si les paramètres sont invalides.
        RuntimeError: Si la création échoue côté Stripe.
    """
    if not STRIPE_API_KEY:
        logger.error("Clé API Stripe manquante.")
        raise RuntimeError("Clé API Stripe manquante.")

    if not isinstance(amount, int) or amount <= 0:
        logger.error("Montant invalide : %s", amount)
        raise ValueError("Montant invalide.")

    try:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            metadata=metadata or {},
            description=description
        )
        logger.info("PaymentIntent créé : %s (%.2f %s)", intent.id, amount / 100, currency)
        return intent.id
    except Exception as e:
        logger.error("Erreur Stripe lors de la création du PaymentIntent : %s", str(e))
        return None

def retrieve_payment_intent(intent_id: str) -> Optional[Dict[str, Any]]:
    """
    Récupère un PaymentIntent Stripe par son ID.

    Args:
        intent_id (str): ID du PaymentIntent.

    Returns:
        dict: Détails du PaymentIntent si succès, None sinon.

    Raises:
        ValueError: Si l’ID est invalide.
    """
    if not intent_id or not isinstance(intent_id, str):
        logger.error("ID PaymentIntent invalide : %s", intent_id)
        raise ValueError("ID PaymentIntent invalide.")

    try:
        intent = stripe.PaymentIntent.retrieve(intent_id)
        logger.info("PaymentIntent récupéré : %s", intent_id)
        return intent
    except Exception as e:
        logger.error("Erreur Stripe lors de la récupération du PaymentIntent : %s", str(e))
        return None