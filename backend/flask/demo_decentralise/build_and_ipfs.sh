#!/bin/bash
# build_and_ipfs.sh – Build statique et publication IPFS (démo décentralisée Dihya)
# Usage : ./build_and_ipfs.sh

set -e

# 1. Générer un build statique (exemple Flask export, à adapter selon le backend)
echo "[Dihya] Export du backend en statique..."
mkdir -p build_demo && cp -r ../../../../backend build_demo/

# 2. Ajouter le build à IPFS
if ! command -v ipfs &> /dev/null; then
  echo "[ERREUR] IPFS n'est pas installé. Installez-le d'abord."
  exit 1
fi

echo "[Dihya] Ajout du build à IPFS..."
CID=$(ipfs add -r build_demo | tail -n1 | awk '{print $2}')
echo "[Dihya] CID IPFS obtenu : $CID"

# 3. Documenter l’accès via une passerelle publique
GATEWAY_URL="https://ipfs.io/ipfs/$CID"
echo "[Dihya] Accès public via : $GATEWAY_URL"
echo $GATEWAY_URL > build_demo/IPFS_GATEWAY_URL.txt

# 4. (Optionnel) Automatiser le backup sur IPFS après chaque déploiement
# (À intégrer dans CI/CD ou post-deploy)

exit 0
