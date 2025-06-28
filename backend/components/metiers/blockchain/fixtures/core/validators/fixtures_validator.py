"""
fixtures_validator.py - Validation avancée des fixtures Blockchain (Python)
"""


def is_valid_blockchain_model(model):
    """Validate blockchain model fixture.

    Args:
        model (dict): The blockchain model fixture to validate.

    Returns:
        bool: True if the fixture is valid, False otherwise.
    """
    return bool(
        model
        and isinstance(model.get("id"), str)
        and isinstance(model.get("vertices"), list)
        and isinstance(model.get("faces"), int)
    )


def is_valid_user(user):
    """Validate user fixture.

    Args:
        user (dict): The user fixture to validate.

    Returns:
        bool: True if the fixture is valid, False otherwise.
    """
    return bool(
        user
        and isinstance(user.get("id"), str)
        and isinstance(user.get("role"), str)
    )
