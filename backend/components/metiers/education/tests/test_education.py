# Test Education

import pytest
from backend.components.metiers.education.schemas import Cours, Utilisateur, Evaluation, Inscription, Programme, EducationProject
from backend.components.metiers.education.utils.sample_util import generer_email_utilisateur, anonymiser_utilisateur
from backend.components.metiers.education.utils.validators import valider_email, valider_note, valider_role, valider_rgpd
from backend.components.metiers.education.plugins import plugin_manager, get_plugin_by_name

def test_cours_schema():
    cours = Cours(id=1, titre="Physique", description="Cours de physique", niveau="L2", enseignant_id=2)
    assert cours.titre == "Physique"
    assert cours.niveau == "L2"

def test_utilisateur_schema():
    user = Utilisateur(id=2, nom="Martin", prenom="Bob", email="bob.martin@example.com", role="enseignant")
    assert user.role == "enseignant"
    assert user.is_active

def test_evaluation_schema():
    eval = Evaluation(id=1, cours_id=1, utilisateur_id=2, note=18.5, commentaire="Excellent", date="2025-06-01")
    assert eval.note > 0
    assert eval.commentaire == "Excellent"

def test_inscription_schema():
    insc = Inscription(id=1, utilisateur_id=2, cours_id=1, date_inscription="2025-06-01", statut="validee")
    assert insc.statut == "validee"

def test_programme_schema():
    cours = [Cours(id=1, titre="Maths", description="", niveau="L1", enseignant_id=1)]
    prog = Programme(id=1, nom="Licence Sciences", description="Programme L1", cours=cours)
    assert len(prog.cours) == 1

def test_education_project_schema():
    project = EducationProject(
        id="1",
        name="Projet Test",
        description="Desc",
        type="ia",
        owner="admin",
        tenant="school",
        createdAt="2025-06-02T00:00:00",
        updatedAt="2025-06-02T00:00:00",
        aiMetadata={"model": "LLaMA"}
    )
    assert project.name == "Projet Test"
    assert project.aiMetadata["model"] == "LLaMA"

def test_generer_email_utilisateur(sample_utilisateur):
    email = generer_email_utilisateur(sample_utilisateur)
    assert "Bienvenue" in email or "bienvenue" in email

def test_anonymiser_utilisateur(sample_utilisateur):
    anon = anonymiser_utilisateur(sample_utilisateur)
    assert anon['email'] == 'anonymized@domain.tld'
    assert anon['nom'] == 'Anonyme'

def test_valider_email():
    assert valider_email('a@b.com')
    assert not valider_email('invalid')

def test_valider_note():
    assert valider_note(15.0)
    assert not valider_note(25.0)

def test_valider_role():
    assert valider_role('etudiant')
    assert not valider_role('hacker')

def test_valider_rgpd(sample_utilisateur):
    assert valider_rgpd(sample_utilisateur.dict())

def test_plugin_exemple(sample_cours):
    plugin = get_plugin_by_name('plugin_exemple')
    assert plugin(sample_cours).startswith('Plugin exécuté')
