import pytest
from ..services import validate_email, validate_phone, validate_rgpd_consent, validate_accessibility

@pytest.mark.parametrize("email", ["test@example.com", "user@domain.fr"])
def test_validate_email(email):
    assert validate_email(email)

@pytest.mark.parametrize("phone", ["+33612345678", "+4915112345678"])
def test_validate_phone(phone):
    assert validate_phone(phone)

def test_validate_rgpd_consent():
    assert validate_rgpd_consent(True)
    assert not validate_rgpd_consent(False)

def test_validate_accessibility():
    assert validate_accessibility({"dummy": True})
