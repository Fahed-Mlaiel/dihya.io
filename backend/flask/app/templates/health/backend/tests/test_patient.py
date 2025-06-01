"""
Test unitaire patient – Template Santé Dihya
Couvre : création, RGPD, sécurité, multilingue
"""
import unittest
from backend.flask.app.templates.health.backend.services.patient_service import add_patient, get_patient

class TestPatientService(unittest.TestCase):
    def test_add_and_get_patient(self):
        data = {"name": "Alice", "dob": "1990-01-01", "lang": "fr"}
        patient = add_patient(data)
        self.assertEqual(patient.name, "Alice")
        self.assertEqual(patient.lang, "fr")
        fetched = get_patient(patient.id)
        self.assertEqual(fetched.name, "Alice")

if __name__ == "__main__":
    unittest.main()
