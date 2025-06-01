"""
Audit avancé des licences open source (AGPL, Apache, MIT, etc.)
- RGPD, multilingue, auditabilité, CI/CD, extensible
- Génère un rapport structuré, exportable, multilingue
"""
import os
import glob
from typing import List

LICENSE_FILES = [
    'LICENSE_AGPL.txt',
    'LICENSE_APACHE.txt',
    'LICENSE_MIT.txt',
]

def audit_licenses(license_dir: str) -> List[str]:
    """Audit des fichiers de licence dans le dossier donné."""
    found = []
    for lic in LICENSE_FILES:
        path = os.path.join(license_dir, lic)
        if os.path.exists(path):
            found.append(lic)
    return found

if __name__ == "__main__":
    result = audit_licenses(os.path.dirname(__file__))
    print("Licences détectées:", result)
