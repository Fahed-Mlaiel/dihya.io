"""
Initialisation du module Web Application Firewall (WAF) custom pour Dihya Coding.

Ce package centralise l’intégration du middleware WAF pour la protection proactive de l’API.
Permet de bloquer les requêtes suspectes (injections, XSS, scans, brute force, etc.) avant qu’elles n’atteignent la logique métier.

Bonnes pratiques :
- Importer ici le middleware principal (waf_middleware)
- Ne jamais exposer de détails techniques sur les blocages dans les réponses
- Prévoir l’extensibilité pour de nouvelles règles ou intégrations (IP dynamique, signatures, etc.)
- Documenter chaque règle ajoutée
"""

from .waf_middleware import waf_middleware