"""
Tests unitaires pour les templates métiers dynamiques de Dihya Coding.

Vérifie la conformité, la structure, la sécurité et l’extensibilité des templates
(e-commerce, éducation, social, etc.) via la fonction get_template_for_domain.
"""

import pytest
from backend.flask.app.services.templates import get_template_for_domain

@pytest.mark.parametrize("domain,expected_keys", [
    ("ecommerce", {"routes", "models", "dependencies", "description"}),
    ("education", {"routes", "models", "dependencies", "description"}),
    ("social", {"routes", "models", "dependencies", "description"}),
])
def test_get_template_for_domain_valid(domain, expected_keys):
    template = get_template_for_domain(domain)
    assert template is not None
    assert set(template.keys()) == expected_keys
    assert isinstance(template["routes"], list)
    assert isinstance(template["models"], list)
    assert isinstance(template["dependencies"], list)
    assert isinstance(template["description"], str)

def test_get_template_for_domain_invalid():
    template = get_template_for_domain("inconnu")
    assert template is None

def test_no_sensitive_data_in_templates():
    # Vérifie qu’aucun champ sensible n’est présent dans les templates
    for domain in ["ecommerce", "education", "social"]:
        template = get_template_for_domain(domain)
        for value in template.values():
            if isinstance(value, str):
                assert "secret" not in value.lower()
                assert "password" not in value.lower()