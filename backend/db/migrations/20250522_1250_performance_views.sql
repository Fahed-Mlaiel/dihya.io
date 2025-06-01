-- Vues pour la performance et l'audit (exemple PostgreSQL)
CREATE OR REPLACE VIEW active_users AS
SELECT id, username, email, role, lang
FROM users
WHERE is_active = TRUE AND deleted_at IS NULL;

CREATE OR REPLACE VIEW audit_last_24h AS
SELECT * FROM audit_logs
WHERE created_at > NOW() - INTERVAL '1 day';
