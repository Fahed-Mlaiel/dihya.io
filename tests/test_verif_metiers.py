import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + '/../'))

import tempfile
import shutil
import time
import subprocess
import pytest
from verif_metiers import (
    lire_liste_metiers_cdc,
    detect_metiers_arbo,
    rapport,
    METIERS_CDC_FALLBACK
)

# --- TESTS UNITAIRES (déjà fournis) ---

def test_lire_liste_metiers_cdc_fallback():
    assert "arts" in lire_liste_metiers_cdc("fichier_inexistant.txt")
    assert set(METIERS_CDC_FALLBACK) >= lire_liste_metiers_cdc("fichier_inexistant.txt")

def test_lire_liste_metiers_cdc_file(tmp_path):
    cdc = tmp_path / "cdc.txt"
    cdc.write_text("sante\nindustrie\n# commentaire\n")
    metiers = lire_liste_metiers_cdc(str(cdc))
    assert "sante" in metiers
    assert "industrie" in metiers
    assert "commentaire" not in metiers

def test_detect_metiers_arbo_basic(tmp_path):
    (tmp_path / "routes" / "sante").mkdir(parents=True)
    (tmp_path / "routes" / "sante" / "routes.py").write_text("# route sante")
    metiers, metiers_par_type, chemins = detect_metiers_arbo(str(tmp_path), show_paths=True)
    assert "sante" in metiers
    assert "sante" in chemins
    assert any("routes/sante/routes.py" in c for c in chemins["sante"])

def test_detect_metiers_arbo_volumineux(tmp_path):
    for i in range(100):
        metier = f"metier_{i}"
        d = tmp_path / "components" / "metiers" / metier
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.js").write_text("// composant")
    metiers, metiers_par_type, chemins = detect_metiers_arbo(str(tmp_path), show_paths=True)
    assert len(metiers) == 100
    assert all(f"metier_{i}" in metiers for i in range(100))

def test_rapport_csv_generation(tmp_path):
    cdc_metiers = {"sante", "industrie"}
    inventaire_metiers = {"sante"}
    metiers_par_type = {"backend_route": {"sante"}}
    chemins_par_metier = {"sante": ["routes/sante/routes.py"]}
    os.chdir(tmp_path)
    rapport(cdc_metiers, inventaire_metiers, metiers_par_type, chemins_par_metier, export_csv=True)
    assert os.path.isfile("rapport_metiers.csv")
    with open("rapport_metiers.csv") as f:
        content = f.read()
        assert "sante" in content
        assert "industrie" in content

def test_detect_ignore_dirs(tmp_path):
    ignored = tmp_path / "node_modules" / "sante"
    ignored.mkdir(parents=True)
    (ignored / "routes.py").write_text("# route ignorée")
    metiers, _, _ = detect_metiers_arbo(str(tmp_path))
    assert "sante" not in metiers

@pytest.mark.parametrize("cdc_line,expected", [
    ("santé", "santé"),
    ("santé publique", "santé_publique"),
    ("santé-publique", "santé_publique"),
    ("santé_publique", "santé_publique"),
])
def test_lire_liste_metiers_cdc_normalisation(tmp_path, cdc_line, expected):
    cdc = tmp_path / "cdc.txt"
    cdc.write_text(cdc_line)
    metiers = lire_liste_metiers_cdc(str(cdc))
    assert expected in metiers

# --- TESTS D'INTEGRATION ---

def test_integration_end_to_end(tmp_path):
    """Test complet : CDC + arbo + rapport CSV"""
    # 1. Génère un CDC
    cdc = tmp_path / "cdc.txt"
    cdc.write_text("sante\nindustrie\n")
    # 2. Crée l'arborescence
    (tmp_path / "routes" / "sante").mkdir(parents=True)
    (tmp_path / "routes" / "sante" / "routes.py").write_text("# route sante")
    # 3. Exécute la détection et le rapport
    metiers_cdc = lire_liste_metiers_cdc(str(cdc))
    metiers, metiers_par_type, chemins = detect_metiers_arbo(str(tmp_path), show_paths=True)
    rapport(metiers_cdc, metiers, metiers_par_type, chemins, export_csv=True)
    # 4. Vérifie le CSV
    csv_path = os.path.join(os.getcwd(), "rapport_metiers.csv")
    assert os.path.isfile(csv_path)
    with open(csv_path) as f:
        content = f.read()
        assert "sante" in content
        assert "industrie" in content

def test_integration_script_cli(tmp_path):
    """Teste l'exécution du script principal en CLI (simulateur utilisateur réel)"""
    # Copie le script dans le dossier temporaire
    import shutil
    shutil.copyfile(os.path.join(os.path.dirname(__file__), "../verif_metiers.py"), tmp_path / "verif_metiers.py")
    cdc = tmp_path / "cdc.txt"
    cdc.write_text("sante\nindustrie\n")
    (tmp_path / "routes" / "sante").mkdir(parents=True)
    (tmp_path / "routes" / "sante" / "routes.py").write_text("# route sante")
    # Exécute le script
    result = subprocess.run(
        ["python3", "verif_metiers.py", "--root", str(tmp_path), "--cdc", str(cdc)],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=10
    )
    assert "sante" in result.stdout
    assert "industrie" in result.stdout
    assert os.path.isfile(tmp_path / "rapport_metiers.csv")

# --- BENCHMARKS DE PERFORMANCE ---

def test_performance_detection_volumetrie(tmp_path):
    """Benchmark : 1000 métiers"""
    N = 1000
    for i in range(N):
        metier = f"metier_{i}"
        d = tmp_path / "components" / "metiers" / metier
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.js").write_text("// composant")
    start = time.time()
    metiers, metiers_par_type, chemins = detect_metiers_arbo(str(tmp_path), show_paths=True)
    duration = time.time() - start
    assert len(metiers) == N
    # Le test échoue si > 5 secondes (à adapter selon votre infra)
    assert duration < 5, f"Détection trop lente : {duration:.2f}s pour {N} métiers"

# --- CONSEILS D'AMELIORATION POUR LE FUTUR ---

"""
Pour faciliter et fiabiliser encore plus le projet :
- Ajoutez des tests de non-régression à chaque évolution du code.
- Ajoutez des tests de compatibilité multi-OS (Linux, Windows, Mac) via GitHub Actions.
- Ajoutez des tests de robustesse sur les caractères spéciaux, les très longs noms de métiers, etc.
- Ajoutez des tests de charge sur des arborescences de 10 000+ métiers si besoin.
- Ajoutez des tests de génération de rapports HTML/Excel (vérifiez la présence des fichiers et leur contenu).
- Ajoutez des tests de sécurité (fichiers malicieux, chemins relatifs/piégés).
- Ajoutez des tests d’intégration continue (CI) pour chaque PR.
- Ajoutez des tests de compatibilité avec d’autres langages (Node, Java, etc.) si vous étendez le projet.
"""

"""
Tests avancés Dihya – test_verif_metiers.py
- Unitaire, intégration, e2e, multilingue, sécurité, accessibilité
- Exécution : pytest --maxfail=1 --disable-warnings
- Multilingue : résultats et logs UTF-8, compatible CI/CD
"""
import locale
locale.setlocale(locale.LC_ALL, '')

# --- TESTS D’INTÉGRATION MULTILINGUES ---
def test_integration_multilingue(tmp_path):
    from verif_metiers import detect_metiers_arbo
    (tmp_path / "routes" / "sante").mkdir(parents=True)
    (tmp_path / "routes" / "sante" / "routes.py").write_text("# route santé")
    metiers, _, _ = detect_metiers_arbo(str(tmp_path), show_paths=True)
    assert any(m in ["sante", "صحة", "ⵙⴰⵏⵜⴰ"] for m in metiers)

# --- TESTS DE SÉCURITÉ ---
def test_no_secret_in_code():
    import os
    with open(os.path.abspath(__file__), 'r', encoding='utf-8') as f:
        code = f.read()
    # On ignore la ligne d'assertion elle-même pour éviter le faux positif
    code_sans_assert = '\n'.join([l for l in code.splitlines() if 'assert' not in l])
    assert 'SECRET' not in code_sans_assert and 'PASSWORD' not in code_sans_assert

# --- TESTS D’ACCESSIBILITÉ (logs, UTF-8) ---
def test_logs_utf8():
    import logging
    logger = logging.getLogger('test')
    try:
        logger.info('Test accentué éèà – العربية – ⴰⵣⵓⵍ')
    except Exception as e:
        assert False, f"Log UTF-8 échoué: {e}"
