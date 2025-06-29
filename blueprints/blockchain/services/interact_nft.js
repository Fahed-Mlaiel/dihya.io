// interact_nft.js – Service d’interaction avancée avec les NFT blockchain

/**
 * Transfère un NFT d’un utilisateur à un autre
 * @param {string} from - Adresse de l’expéditeur
 * @param {string} to - Adresse du destinataire
 * @param {string} tokenId - Identifiant du NFT
 * @returns {Object} Résultat du transfert
 */
function transferNFT(from, to, tokenId) {
  if (!from || !to || !tokenId) throw new Error('Paramètres manquants');
  // Logique simulée
  return {
    success: true,
    from,
    to,
    tokenId,
    txHash: '0x' + tokenId + Date.now()
  };
}

/**
 * Récupère les métadonnées d’un NFT
 * @param {string} tokenId
 * @returns {Object} Métadonnées simulées
 */
function getNFTMetadata(tokenId) {
  if (!tokenId) throw new Error('tokenId manquant');
  return {
    tokenId,
    name: 'NFT #' + tokenId,
    description: 'NFT simulé pour test',
    image: 'https://dummyimage.com/600x400/000/fff&text=NFT+' + tokenId
  };
}

module.exports = { transferNFT, getNFTMetadata };
