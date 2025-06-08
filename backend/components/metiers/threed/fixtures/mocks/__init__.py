"""
Init du module mocks (Python)
"""
from .core import *
from .samples import *
from .fixtures_mock import mock_request, mock_response

__all__ = ['mock_request', 'mock_response']
