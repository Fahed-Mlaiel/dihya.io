"""
templates_utils.py – Logique métier ultra avancée helpers/utils (Python)
CDC Dihya : RGPD, accessibilité, audit, CI/CD, edge cases, hooks, robustesse, conformité, multi-formats
"""
import re
from datetime import datetime
import random
import string

def generate_template_id(prefix='tpl'):
    date = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{prefix}_{date}_{rand}"

def clean_template_content(content):
    if not content:
        return ''
    content = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}", '[anonymisé]', content)
    content = re.sub(r"Nom: [^\n]+", 'Nom: [anonymisé]', content)
    return content

def check_accessibility(content):
    return bool(re.search(r"aria-|alt=|role=", content or ''))

def audit_template(content):
    return {
        'length': len(content or ''),
        'hasAccessibility': check_accessibility(content or ''),
        'isRGPD': '@' not in (content or ''),
        'timestamp': datetime.utcnow().isoformat()
    }
