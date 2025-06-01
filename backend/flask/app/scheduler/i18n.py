"""
Internationalisation (i18n) pour le module Scheduler.
Support multilingue, extensible, production-ready.
"""

TRANSLATIONS = {
    "fr": {
        "job_created": "Job planifié créé avec succès.",
        "job_updated": "Job planifié mis à jour.",
        "job_deleted": "Job planifié supprimé.",
        "job_run": "Job exécuté."
    },
    "en": {
        "job_created": "Scheduled job created successfully.",
        "job_updated": "Scheduled job updated.",
        "job_deleted": "Scheduled job deleted.",
        "job_run": "Job executed."
    }
}

def translate(key, lang="fr"):
    return TRANSLATIONS.get(lang, TRANSLATIONS["fr"]).get(key, key)
