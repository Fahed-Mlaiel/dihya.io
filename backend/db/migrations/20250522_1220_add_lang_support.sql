-- Ajout du support multilingue (fr, en, ar, tzm)
ALTER TABLE users ADD COLUMN IF NOT EXISTS lang VARCHAR(8) NOT NULL DEFAULT 'fr';
-- Mise à jour des utilisateurs existants (si besoin)
UPDATE users SET lang='fr' WHERE lang IS NULL;
