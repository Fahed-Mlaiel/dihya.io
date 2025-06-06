# sample_usage.py
"""Exemple d'utilisation du module validators (Python)"""
from ..core import validators
import json
with open('sample_validators_data.json') as f:
    data = json.load(f)

print('Email valide ?', validators.validate_email(data['email']))
print('Champ obligatoire valide ?', validators.validate_required(data['requiredField']))
