"""
Dihya – Django Banque & Finance I18N Ultra Avancé
-------------------------------------------------
- Messages multilingues (fr, en, ar, tzm) pour API, logs, erreurs, notifications
"""
I18N = {
    'fr': {
        'compte_introuvable': "Compte introuvable",
        'unauthorized': "Accès non autorisé",
        'solde': "Solde du compte : {solde} {devise}"
    },
    'en': {
        'compte_introuvable': "Account not found",
        'unauthorized': "Unauthorized access",
        'solde': "Account balance: {solde} {devise}"
    },
    'ar': {
        'compte_introuvable': "الحساب غير موجود",
        'unauthorized': "دخول غير مصرح به",
        'solde': "رصيد الحساب: {solde} {devise}"
    },
    'tzm': {
        'compte_introuvable': "Abrid ur yufa ara",
        'unauthorized': "Anekcum ur yettwasir ara",
        'solde': "Abrid n umidag: {solde} {devise}"
    }
}
