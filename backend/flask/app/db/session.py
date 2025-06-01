"""
session.py — Initialisation DB Dihya Coding (Flask)
Connexion, session, sécurité, RGPD, auditabilité
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DB_URL = os.getenv("DIHYA_DB_URL", "sqlite:///dihya.db")
engine = create_engine(DB_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
