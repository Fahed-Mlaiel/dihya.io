# Script shell de génération de documentation pour le module voyage
# Usage: ./gen_doc.sh
# Génère la documentation technique et métier à partir des sources et templates.

python ../../../gen_doc_metiers.py --module voyage --output ./DOC_VOYAGE.md
