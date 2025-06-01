import os
import django
import pytest

def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dihya.backend.django.settings')
    django.setup()
