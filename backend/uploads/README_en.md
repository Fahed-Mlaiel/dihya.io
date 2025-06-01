# Dihya Backend Uploads – English Documentation

This folder manages user-uploaded files (documents, images, etc.) for the Dihya backend.

## Features
- Security, GDPR, accessibility, sovereignty
- Logging, processing, rejection, logs
- Multilingual (fr, en, ar, tzm)

## Structure
- logs/: upload, audit, GDPR logs
- processed/: validated and processed files
- rejected/: rejected files (virus, extension, GDPR)
- temp/: temporary files

## Best practices
- Scan every uploaded file
- Limit file size and type
- Log every action
- Regularly purge

---

> See main documentation in `../README.md` and scripts in `../../scripts/`.
