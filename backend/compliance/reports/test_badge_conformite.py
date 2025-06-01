"""
Tests avancés pour la génération, l’accessibilité et la conformité du badge SVG de conformité Dihya.
Couvre : multilingue, accessibilité ARIA, CI/CD, RGPD, plugins, audit, intégration CI, auditabilité, export, fallback, sécurité.
"""
import pytest
from badge_conformite import generer_badge_conformite
from xml.etree import ElementTree as ET
import re

@pytest.mark.parametrize("langue,etat", [
    ("fr", "conforme"), ("en", "conforme"), ("ar", "conforme"), ("ber", "conforme"),
    ("de", "conforme"), ("zh", "conforme"), ("ja", "conforme"), ("ko", "conforme"),
    ("nl", "conforme"), ("he", "conforme"), ("fa", "conforme"), ("hi", "conforme"), ("es", "conforme"),
    ("fr", "non conforme"), ("fr", "audit"), ("fr", "en attente")
])
def test_badge_svg_accessible(langue, etat):
    svg = generer_badge_conformite(etat=etat, langue=langue, ci=True, acces_aria=True)
    # Vérifie que le SVG est bien formé
    try:
        root = ET.fromstring(svg)
    except Exception as e:
        pytest.fail(f"SVG mal formé: {e}")
    # Vérifie la présence de l'attribut ARIA et du <desc>
    assert 'aria-label' in svg
    assert '<desc>' in svg
    # Vérifie la présence du label dans la langue
    assert any(lbl in svg for lbl in ["Conforme", "Compliant", "متوافق", "ⴰⵙⵉⵏⴼⴰⵡ", "Konform", "合规", "準拠", "준수", "Conform", "תואם", "مطابق", "अनुपालन", "Conforme"])
    # Vérifie la présence de l’état
    assert etat.capitalize() in svg or etat in svg
    # Vérifie la présence de la date
    assert re.search(r"\d{4}-\d{2}-\d{2}", svg)
    # Vérifie la présence de l’icône CI/CD
    assert 'CI' in svg
    # Vérifie la présence de la coche
    assert '✓' in svg

def test_badge_svg_plugin():
    svg = generer_badge_conformite(etat="conforme", langue="fr", plugin="audit-pro", ci=True)
    assert "audit-pro" in svg

def test_badge_svg_no_aria():
    svg = generer_badge_conformite(etat="conforme", langue="fr", acces_aria=False)
    assert 'aria-label' not in svg
    assert '<desc>' not in svg

def test_badge_svg_export(tmp_path):
    svg = generer_badge_conformite(etat="conforme", langue="fr")
    f = tmp_path / "badge.svg"
    f.write_text(svg, encoding="utf-8")
    # Relit le fichier et vérifie
    content = f.read_text(encoding="utf-8")
    assert '<svg' in content
    assert 'Conforme' in content

def test_badge_svg_security():
    svg = generer_badge_conformite(etat="conforme", langue="fr")
    # Pas de script ou d’élément dangereux
    assert '<script' not in svg
    assert 'onload' not in svg
    assert 'javascript:' not in svg

def test_badge_svg_fallback():
    # Langue inconnue => fallback fr
    svg = generer_badge_conformite(etat="conforme", langue="xx")
    assert 'Conforme' in svg

def test_badge_svg_auditabilite():
    svg = generer_badge_conformite(etat="audit", langue="fr")
    assert 'Audit' in svg or 'audit' in svg

def test_badge_svg_multitenant():
    svg1 = generer_badge_conformite(etat="conforme", langue="fr", plugin="tenant1")
    svg2 = generer_badge_conformite(etat="conforme", langue="fr", plugin="tenant2")
    assert svg1 != svg2

def test_badge_svg_ci_toggle():
    svg = generer_badge_conformite(etat="conforme", langue="fr", ci=False)
    assert 'CI' not in svg

def test_badge_svg_accessibility_contrast():
    svg = generer_badge_conformite(etat="conforme", langue="fr")
    # Vérifie le contraste (vert sur blanc)
    assert '#2ecc40' in svg or '#fff' in svg
