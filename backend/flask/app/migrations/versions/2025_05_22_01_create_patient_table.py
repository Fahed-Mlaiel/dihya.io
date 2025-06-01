"""
Migration Alembic – Création table patient (Dihya)
But : ajouter la table patient pour le template santé
Date : 2025-05-22
Rollback : suppression de la table
Logs : horodatage, audit, RGPD
"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

def upgrade():
    op.create_table(
        'patient',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(128), nullable=False),
        sa.Column('dob', sa.Date, nullable=False),
        sa.Column('lang', sa.String(8), nullable=False, default='fr'),
        sa.Column('created_at', sa.DateTime, default=datetime.utcnow),
    )
    print(f"[MIGRATION] Table patient créée – {datetime.utcnow()}")

def downgrade():
    op.drop_table('patient')
    print(f"[MIGRATION] Table patient supprimée – {datetime.utcnow()}")
