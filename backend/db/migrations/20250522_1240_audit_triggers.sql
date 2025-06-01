-- Déclencheurs d'audit pour journaliser les modifications critiques (exemple PostgreSQL)
CREATE OR REPLACE FUNCTION log_user_update() RETURNS trigger AS $$
BEGIN
  INSERT INTO audit_logs(user_id, action, details)
  VALUES (NEW.id, 'update_user', row_to_json(NEW));
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_user_update ON users;
CREATE TRIGGER trg_user_update
AFTER UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION log_user_update();
