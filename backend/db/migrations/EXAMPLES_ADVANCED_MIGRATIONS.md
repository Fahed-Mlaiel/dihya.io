# Exemples d’utilisation avancés – Migrations Dihya DB

## 1. Script Python Alembic (upgrade/downgrade)

```python
# migrations/20250523_1300_add_audit_table.py
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'audit_log',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('action', sa.String(128), nullable=False),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('timestamp', sa.DateTime, server_default=sa.func.now()),
        sa.Column('lang', sa.String(8), nullable=False, server_default='fr')
    )

def downgrade():
    op.drop_table('audit_log')
```

## 2. Utilisation CI/CD (GitHub Actions)

```yaml
jobs:
  migrate-db:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        ports: [5432:5432]
        env:
          POSTGRES_USER: dihya
          POSTGRES_PASSWORD: dihya
          POSTGRES_DB: dihya
    steps:
      - uses: actions/checkout@v4
      - name: Installer dépendances
        run: pip install alembic psycopg2-binary
      - name: Appliquer les migrations
        run: alembic upgrade head
      - name: Rollback (exemple)
        run: alembic downgrade -1
```

## 3. Rollback manuel (bash)

```bash
# Appliquer la dernière migration
alembic upgrade head
# Revenir en arrière d’un cran
alembic downgrade -1
```

## 4. Migration multilingue (SQL)

```sql
ALTER TABLE users ADD COLUMN lang VARCHAR(8) DEFAULT 'fr';
UPDATE users SET lang = 'fr' WHERE lang IS NULL;
```
