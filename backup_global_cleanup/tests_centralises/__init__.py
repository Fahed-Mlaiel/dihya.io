"""
Initialisation avancée des tests Python pour tests_centralises
"""
import unittest
import os

def run_all_tests():
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.dirname(__file__))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result

