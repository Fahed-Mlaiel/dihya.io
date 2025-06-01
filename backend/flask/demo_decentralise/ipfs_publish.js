// ipfs_publish.js – Publication IPFS automatisée (Node.js, démo décentralisée Dihya)
const { execSync } = require('child_process');
const path = require('path');

function publishToIPFS(dir = './build_demo') {
  try {
    console.log('[Dihya] Ajout du build à IPFS...');
    const result = execSync(`ipfs add -r ${dir}`, { encoding: 'utf-8' });
    const lines = result.trim().split('\n');
    const lastLine = lines[lines.length - 1];
    const cid = lastLine.split(' ')[1];
    const gatewayUrl = `https://ipfs.io/ipfs/${cid}`;
    console.log(`[Dihya] CID IPFS obtenu : ${cid}`);
    console.log(`[Dihya] Accès public via : ${gatewayUrl}`);
    return gatewayUrl;
  } catch (err) {
    console.error('[ERREUR] Publication IPFS échouée :', err.message);
    return null;
  }
}

module.exports = { publishToIPFS };

// Exemple d'utilisation :
// const { publishToIPFS } = require('./ipfs_publish');
// publishToIPFS();
