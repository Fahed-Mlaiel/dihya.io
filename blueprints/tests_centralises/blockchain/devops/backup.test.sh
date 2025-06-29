#!/bin/bash
set -e

# Test nominal : backup.sh doit s'exécuter sans erreur
/workspaces/dihya.io/blueprints/blockchain/devops/backup.sh
if [ $? -eq 0 ]; then
  echo "Backup nominal : OK"
else
  echo "Backup nominal : FAIL"
  exit 1
fi

# Test edge case : backup sur dossier inexistant
if /workspaces/dihya.io/blueprints/blockchain/devops/backup.sh /tmp/folder_that_does_not_exist; then
  echo "Backup edge case : FAIL"
  exit 1
else
  echo "Backup edge case : OK"
fi
