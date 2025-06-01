import pytest

@pytest.fixture
def validation_datasets_report():
    return {
  "date": "2025-05-22T12:46:42.683131Z",
  "files": [
    {
      "file": "audit_events_sample.json",
      "valid": true,
      "errors": []
    },
    {
      "file": "users_sample.json",
      "valid": true,
      "errors": []
    },
    {
      "file": "validation_datasets_report.json",
      "valid": false,
      "errors": [
        "Format JSON attendu: liste"
      ]
    },
    {
      "file": "users_sample_full.yaml",
      "valid": true,
      "errors": []
    },
    {
      "file": "transactions_sample.csv",
      "valid": false,
      "errors": [
        "Email manquant ou invalide"
      ]
    },
    {
      "file": "audit_events_sample_full.yaml",
      "valid": true,
      "errors": []
    },
    {
      "file": "users_sample_full.json",
      "valid": true,
      "errors": []
    },
    {
      "file": "audit_events_sample.csv",
      "valid": false,
      "errors": [
        "Email manquant ou invalide"
      ]
    },
    {
      "file": "users_sample.csv",
      "valid": true,
      "errors": []
    },
    {
      "file": "transactions_sample_full.csv",
      "valid": false,
      "errors": [
        "Email manquant ou invalide"
      ]
    },
    {
      "file": "audit_events_sample_full.json",
      "valid": true,
      "errors": []
    },
    {
      "file": "transactions_sample.json",
      "valid": true,
      "errors": []
    },
    {
      "file": "transactions_sample.yaml",
      "valid": true,
      "errors": []
    },
    {
      "file": "transactions_sample_full.yaml",
      "valid": true,
      "errors": []
    },
    {
      "file": "audit_events_sample.yaml",
      "valid": true,
      "errors": []
    },
    {
      "file": "users_sample.yaml",
      "valid": true,
      "errors": []
    },
    {
      "file": "transactions_sample_full.json",
      "valid": true,
      "errors": []
    }
  ]
}
