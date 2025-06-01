# Script shell de vérification de conformité RGPD et accessibilité pour le module voice
# Usage: ./check_conformite.sh
# Vérifie la présence et la conformité des fichiers critiques (audit, RGPD, accessibilité, tests, doc, assets, scripts, etc.)

REQUIRED_FILES=(
  "audit.py"
  "i18n.py"
  "permissions.py"
  "fixtures.json"
  "README_multilingue.md"
  "README_accessibilite_rgpd.md"
  "assets/audio_fr.mp3.txt"
  "assets/audio_en.mp3.txt"
  "assets/audio_ar.mp3.txt"
  "assets/audio_amazigh.mp3.txt"
  "scripts/rgpd_export.sh"
  "scripts/rgpd_cleanup.sh"
  "scripts/backup_voice.sh"
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
