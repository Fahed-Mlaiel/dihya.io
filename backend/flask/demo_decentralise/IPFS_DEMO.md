# IPFS_DEMO.md – Déploiement décentralisé Dihya (IPFS, DWeb)

Ce dossier contient :
- `build_and_ipfs.sh` : script Bash pour exporter le backend et publier sur IPFS (build statique, CID, accès passerelle).
- `ipfs_publish.js` : script Node.js pour automatiser la publication IPFS (intégrable CI/CD, monitoring, logs).
- `index.js` : point d’entrée modulaire pour la démo décentralisée.
- `README.md` : documentation complète, workflow, sécurité, bonnes pratiques.

## Utilisation rapide

### Bash
```bash
cd backend/flask/demo_decentralise
chmod +x build_and_ipfs.sh
./build_and_ipfs.sh
# Le CID IPFS et l’URL passerelle sont affichés et sauvegardés dans build_demo/IPFS_GATEWAY_URL.txt
```

### Node.js
```js
const { publishToIPFS } = require('./ipfs_publish');
const url = publishToIPFS();
console.log('URL IPFS:', url);
```

## Sécurité & conformité
- Ne jamais publier de secrets ou données sensibles.
- Vérifier l’intégrité des fichiers publiés.
- Protéger les endpoints critiques même en environnement décentralisé.
- Documenter chaque étape et automatiser les backups si besoin.

## Intégration CI/CD
- Ajoutez l’appel à `build_and_ipfs.sh` ou `ipfs_publish.js` dans vos workflows GitHub Actions, GitLab CI, etc.

---

**Dihya Coding – Décentralisation, souveraineté, audit, sécurité, documentation intégrée.**
