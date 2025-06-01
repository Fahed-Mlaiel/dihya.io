"""
Internationalisation pour le module Health (i18n, multilingue, accessibilité)
"""
I18N_LABELS = {
    'fr': {
        'patient': 'Patient',
        'diagnostic': 'Diagnostic',
        'date_consultation': 'Date de consultation',
    },
    'en': {
        'patient': 'Patient',
        'diagnostic': 'Diagnosis',
        'date_consultation': 'Consultation Date',
    }
}

def get_label(field, lang='fr'):
    return I18N_LABELS.get(lang, I18N_LABELS['fr']).get(field, field)
