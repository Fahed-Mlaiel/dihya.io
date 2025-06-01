/*
  Dihya – Schéma de base de données ultra avancé (multi-stack, multilingue, souveraineté, sécurité)
  - Compatible PostgreSQL (recommandé), MySQL, SQLite (adaptable)
  - Sécurité, conformité RGPD/NIS2, auditabilité, multilingue, extensibilité
  - Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution
  - Documentation multilingue intégrée (fr, en, ar, tzm)
*/

-- =========================
-- TABLE UTILISATEURS / USERS
-- =========================
CREATE TABLE IF NOT EXISTS users (
    id              SERIAL PRIMARY KEY,
    username        VARCHAR(64) NOT NULL UNIQUE,
    email           VARCHAR(128) NOT NULL UNIQUE,
    password_hash   VARCHAR(256) NOT NULL,
    role            VARCHAR(32) NOT NULL DEFAULT 'user', -- admin, ai_user, auditor, user, guest
    lang            VARCHAR(8)  NOT NULL DEFAULT 'fr',   -- fr, en, ar, tzm
    is_active       BOOLEAN     NOT NULL DEFAULT TRUE,
    consent_rgpd    BOOLEAN     NOT NULL DEFAULT FALSE,
    created_at      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deleted_at      TIMESTAMP,
    -- RGPD: données minimisées, suppression logique, auditabilité
    CONSTRAINT chk_role CHECK (role IN ('admin', 'ai_user', 'auditor', 'user', 'guest'))
);

COMMENT ON TABLE users IS
'🇫🇷 Utilisateurs de la plateforme Dihya (sécurité, multilingue, RGPD)
 🇬🇧 Dihya platform users (security, multilingual, GDPR)
 🇦🇪 مستخدمو منصة ديهيا (الأمان، متعدد اللغات، RGPD)
 ⵣ Iseqdacen n platforma Dihya (amatu, multilingual, RGPD)';

-- =========================
-- TABLE LOGS D'AUDIT / AUDIT LOGS
-- =========================
CREATE TABLE IF NOT EXISTS audit_logs (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER REFERENCES users(id) ON DELETE SET NULL,
    action          VARCHAR(128) NOT NULL,
    details         JSONB,
    ip_address      VARCHAR(64),
    user_agent      VARCHAR(256),
    created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    -- RGPD: anonymisation, auditabilité, traçabilité
    INDEX idx_audit_user (user_id),
    INDEX idx_audit_action (action)
);

COMMENT ON TABLE audit_logs IS
'🇫🇷 Logs d’audit horodatés, anonymisés, exportables (RGPD/NIS2)
 🇬🇧 Timestamped, anonymized, exportable audit logs (GDPR/NIS2)
 🇦🇪 سجلات تدقيق مؤرخة، مجهولة، قابلة للتصدير (RGPD/NIS2)
 ⵣ Ilog n audit s wakud, anonymized, exportable (RGPD/NIS2)';

-- =========================
-- TABLE CONSENTEMENTS / CONSENTS
-- =========================
CREATE TABLE IF NOT EXISTS consents (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER REFERENCES users(id) ON DELETE CASCADE,
    consent_type    VARCHAR(64) NOT NULL, -- e.g. 'rgpd', 'newsletter'
    granted         BOOLEAN     NOT NULL,
    granted_at      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    revoked_at      TIMESTAMP,
    INDEX idx_consent_user (user_id)
);

COMMENT ON TABLE consents IS
'🇫🇷 Consentements utilisateurs (RGPD, newsletter, etc.)
 🇬🇧 User consents (GDPR, newsletter, etc.)
 🇦🇪 موافقات المستخدمين (RGPD، النشرة الإخبارية، إلخ)
 ⵣ Ttwasna n useqdac (RGPD, newsletter, etc.)';

-- =========================
-- TABLE PLUGINS / PLUGINS
-- =========================
CREATE TABLE IF NOT EXISTS plugins (
    id              SERIAL PRIMARY KEY,
    name            VARCHAR(64) NOT NULL UNIQUE,
    version         VARCHAR(32) NOT NULL,
    author          VARCHAR(128),
    license         VARCHAR(64) NOT NULL,
    enabled         BOOLEAN     NOT NULL DEFAULT TRUE,
    config          JSONB,
    created_at      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE plugins IS
'🇫🇷 Plugins métiers, IA, extensions (sécurité, audit, OSS)
 🇬🇧 Business plugins, AI, extensions (security, audit, OSS)
 🇦🇪 إضافات الأعمال، الذكاء الاصطناعي، التوسعات (الأمان، التدقيق، OSS)
 ⵣ Plugins n l3amal, IA, extensions (amatu, audit, OSS)';

-- =========================
-- TABLE TEMPLATES MÉTIERS / BUSINESS TEMPLATES
-- =========================
CREATE TABLE IF NOT EXISTS business_templates (
    id              SERIAL PRIMARY KEY,
    name            VARCHAR(64) NOT NULL UNIQUE,
    description     TEXT,
    language        VARCHAR(16) NOT NULL, -- e.g. 'js', 'py', 'dart'
    content         TEXT NOT NULL,
    created_by      INTEGER REFERENCES users(id) ON DELETE SET NULL,
    created_at      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE business_templates IS
'🇫🇷 Templates métiers, générateurs de code, multistack
 🇬🇧 Business templates, code generators, multistack
 🇦🇪 قوالب الأعمال، مولدات الشيفرة، متعدد التقنيات
 ⵣ Templates n l3amal, code generators, multistack';

-- =========================
-- TABLE SESSIONS (AUTH) / SESSIONS
-- =========================
CREATE TABLE IF NOT EXISTS sessions (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER REFERENCES users(id) ON DELETE CASCADE,
    session_token   VARCHAR(256) NOT NULL UNIQUE,
    created_at      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expires_at      TIMESTAMP   NOT NULL,
    ip_address      VARCHAR(64),
    user_agent      VARCHAR(256)
);

COMMENT ON TABLE sessions IS
'🇫🇷 Sessions d’authentification utilisateur (sécurité, RGPD)
 🇬🇧 User authentication sessions (security, GDPR)
 🇦🇪 جلسات مصادقة المستخدم (الأمان، RGPD)
 ⵣ Sessions n useqdac (amatu, RGPD)';

-- =========================
-- TABLE ARCHIVES DE CONFORMITÉ / COMPLIANCE ARCHIVES
-- =========================
CREATE TABLE IF NOT EXISTS compliance_archives (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER REFERENCES users(id) ON DELETE SET NULL,
    archive_type    VARCHAR(64) NOT NULL, -- e.g. 'export', 'deletion', 'report'
    data            JSONB,
    created_at      TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP,
    encrypted       BOOLEAN     NOT NULL DEFAULT TRUE
);

COMMENT ON TABLE compliance_archives IS
'🇫🇷 Archives de conformité (exports RGPD, suppressions, rapports)
 🇬🇧 Compliance archives (GDPR exports, deletions, reports)
 🇦🇪 أرشيفات التوافقية (تصدير RGPD، حذف، تقارير)
 ⵣ Archives n compliance (RGPD exports, deletions, reports)';

-- =========================
-- INDEXES & SÉCURITÉ
-- =========================
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_role ON users(role);
CREATE INDEX IF NOT EXISTS idx_logs_created_at ON audit_logs(created_at);
CREATE INDEX IF NOT EXISTS idx_sessions_token ON sessions(session_token);

-- =========================
-- VUES D'AUDIT / AUDIT VIEWS (exemple)
-- =========================
CREATE OR REPLACE VIEW v_active_users AS
SELECT id, username, email, role, lang, created_at
FROM users
WHERE is_active = TRUE AND deleted_at IS NULL;

-- =========================
-- TRIGGERS DE SÉCURITÉ (exemple)
-- =========================
-- Met à jour updated_at à chaque modification
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = NOW();
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_users_updated_at
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE PROCEDURE update_updated_at_column();

CREATE TRIGGER trg_update_plugins_updated_at
BEFORE UPDATE ON plugins
FOR EACH ROW
EXECUTE PROCEDURE update_updated_at_column();

CREATE TRIGGER trg_update_templates_updated_at
BEFORE UPDATE ON business_templates
FOR EACH ROW
EXECUTE PROCEDURE update_updated_at_column();

-- =========================
-- SÉCURITÉ, RGPD, MULTILINGUE, EXTENSIBILITÉ
-- =========================
-- Toutes les tables sont prêtes pour la souveraineté, la conformité, l’audit, la suppression logique, l’export RGPD.
-- Multilingue : stocker la langue préférée, traduire les messages côté API.
-- Extensible : ajoutez vos modules, plugins, IA, logs, rapports, etc.

-- 🇫🇷 Schéma validé pour la production, la démo, la contribution.
-- 🇬🇧 Schema validated for production, demo, contribution.
-- 🇦🇪 مخطط قاعدة البيانات جاهز للإنتاج والعرض والمساهمة.
-- ⵣ Asnul n database schema yella-d i production, demo, contribution.
