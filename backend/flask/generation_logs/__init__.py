"""
Module pour la traçabilité et l’horodatage des générations de code dans Dihya Coding.

Ce package permet de journaliser chaque génération de projet (frontend, backend, assets, etc.)
avec un log horodaté, le type de génération, l’utilisateur (si applicable) et les métadonnées associées.

Bonnes pratiques :
- Chaque log doit inclure la date, l’heure, le type de génération, l’auteur (si connu) et un identifiant unique.
- Ne jamais stocker de secrets ou de données sensibles dans les logs.
- Prévoir une rotation et une purge régulière des logs.
- Les logs doivent être accessibles uniquement aux administrateurs ou à des fins d’audit.

Exemple d’utilisation :
    from generation_logs import log_generation_event
    log_generation_event("backend", user="alice", meta={"stack": "Flask"})

"""

import os
from datetime import datetime
import json
import uuid

def log_generation_event(*args, **kwargs):
    pass

LOG_FILE = "/tmp/generation.log"

def log_generation_event(event_type, user=None, meta=None, sector=None):
    """
    Journalise un événement de génération de code, sectorisé.
    :param event_type: Type de génération (ex: backend, frontend, ia, etc.)
    :param user: Utilisateur à l’origine de la génération (optionnel)
    :param meta: Dictionnaire de métadonnées complémentaires (optionnel)
    :param sector: Secteur métier (optionnel)
    """
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_id": str(uuid.uuid4()),
        "event_type": event_type,
        "user": user,
        "meta": meta or {},
        "sector": sector
    }
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
    # Appel des hooks métier si présents
    if hasattr(add_generation_hook, '_GENERATION_HOOKS'):
        for hook in add_generation_hook._GENERATION_HOOKS:
            try:
                hook(log_entry)
            except Exception:
                continue


def add_generation_hook(hook_func):
    """
    Permet d’ajouter un hook métier appelé après chaque log de génération.
    :param hook_func: Fonction à appeler avec le log_entry en paramètre
    """
    global _GENERATION_HOOKS
    if not hasattr(add_generation_hook, '_GENERATION_HOOKS'):
        add_generation_hook._GENERATION_HOOKS = []
    add_generation_hook._GENERATION_HOOKS.append(hook_func)


def export_logs_to_ipfs(ipfs_client=None):
    """
    Exporte les logs de génération sur IPFS (DWeb) pour audit souverain.
    :param ipfs_client: Client IPFS (optionnel)
    """
    if not os.path.exists(LOG_FILE):
        return None
    with open(LOG_FILE, 'rb') as f:
        data = f.read()
    if ipfs_client:
        return ipfs_client.add_bytes(data)
    # Placeholder: à adapter selon l’API IPFS utilisée
    return data


def purge_old_logs(days=30):
    """
    Purge les logs de génération plus anciens que N jours.
    """
    import time
    if not os.path.exists(LOG_FILE):
        return
    cutoff = time.time() - days * 86400
    lines = []
    with open(LOG_FILE, encoding='utf-8') as f:
        for line in f:
            try:
                entry = json.loads(line)
                ts = datetime.fromisoformat(entry['timestamp']).timestamp()
                if ts > cutoff:
                    lines.append(line)
            except Exception:
                continue
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.writelines(lines)


def anonymize_log_entry(entry):
    """
    Anonymise les champs sensibles d’un log pour conformité RGPD.
    """
    entry = dict(entry)
    entry['user'] = None
    if 'meta' in entry:
        for k in list(entry['meta'].keys()):
            if k in {'email', 'phone', 'ip', 'token', 'password', 'api_key'}:
                del entry['meta'][k]
    return entry

# Validation automatique de la cohérence des logs (exemple)
def validate_log_coherence(entry):
    """
    Valide la cohérence métier d’un log (structure, unicité, conformité RGPD).
    """
    assert 'timestamp' in entry and 'event_id' in entry and 'event_type' in entry
    assert isinstance(entry['meta'], dict)
    # RGPD : pas de secrets ni de données sensibles
    for k in entry['meta']:
        assert k not in {'password', 'api_key', 'token'}
    return True

# Exemple d’utilisation sectorielle avancée
def log_generation_event_sector(event_type, user=None, meta=None, sector=None):
    """
    Journalise un événement de génération sectorisé (santé, éducation, ecommerce, etc.).
    """
    log_generation_event(event_type, user=user, meta=meta, sector=sector)
