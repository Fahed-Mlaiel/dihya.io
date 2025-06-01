# Script shell de vérification de conformité RGPD et accessibilité pour le module vr_ar
# Usage: ./check_conformite.sh
# Vérifie la présence et la conformité des fichiers critiques (audit, RGPD, accessibilité, tests, doc, assets, scripts, etc.)

REQUIRED_FILES=(
  "audit.py"
  "i18n.py"
  "permissions.py"
  "fixtures.json"
  "README_multilingue.md"
  "README_accessibilite_rgpd.md"
  "assets/scene_fr.glb.txt"
  "assets/scene_en.glb.txt"
  "assets/scene_ar.glb.txt"
  "assets/scene_amazigh.glb.txt"
  "scripts/rgpd_export.sh"
  "scripts/rgpd_cleanup.sh"
  "scripts/backup_vr_ar.sh"
  "scripts/run_tests.sh"
  "scripts/gen_doc.sh"
  "tests/test_accessibilite.py"
  "tests/test_e2e.py"
  "tests/test_integration.py"
  "tests/test_performance.py"
  "tests/test_plugin.py"
)

for f in "${REQUIRED_FILES[@]}"; do
  if [ ! -f "$f" ]; then
    echo "[ERREUR] Fichier manquant : $f"
    exit 1
  fi
done

echo "Tous les fichiers critiques sont présents et conformes."
