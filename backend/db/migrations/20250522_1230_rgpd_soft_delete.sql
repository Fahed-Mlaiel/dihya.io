-- Ajout de la suppression logique (soft delete) pour conformité RGPD
ALTER TABLE users ADD COLUMN IF NOT EXISTS deleted_at TIMESTAMP;
