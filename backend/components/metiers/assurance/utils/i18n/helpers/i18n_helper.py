# i18n_helper.py
# Helper i18n Python pour Assurance – exemple clé en main


def humanize_key(key):
    """
    Transforme une clé i18n en format lisible (ex: 'HELLO_WORLD' => 'Hello world')
    """
    if not key:
        return ""
    return key.replace("_", " ").capitalize().lower()
