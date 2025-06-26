"""
Secrets DevOps threed (Python)
"""


def get_secret(key):
    import os

    return os.environ.get(key)
