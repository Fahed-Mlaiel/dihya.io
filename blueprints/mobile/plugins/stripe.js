// Plugin Stripe avancé avec simulation de paiement, gestion d’erreur, callback
export function payWithStripe(amount, onSuccess, onError) {
  if (amount <= 0) {
    if (onError) onError('Montant invalide');
    return;
  }
  // Simule un paiement Stripe
  setTimeout(() => {
    if (onSuccess) onSuccess({ status: 'success', amount });
  }, 1000);
}
// Exemple d’intégration : payWithStripe(100, res => alert('Payé!'), err => alert(err))
