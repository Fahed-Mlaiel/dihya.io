# Dihya Backend Storage – English Documentation

This folder manages file, blob, document, upload, and backup storage for the Dihya backend.

## Features
- Secure, sovereign, auditable storage
- Multi-backend support (local, S3, MinIO, sovereign cloud)
- GDPR compliance (logs, purge, anonymization)
- Accessibility and multilingual (fr, en, ar, tzm)

## Structure
- uploads/: user-uploaded files
- backups/: encrypted backups
- temp/: temporary files, auto-cleaned
- logs/: access and audit logs

## Best practices
- Always encrypt sensitive data
- Restrict access (RBAC, logs)
- Regularly purge temporary files

---

> See main documentation in `../README.md` and scripts in `../scripts/`.
