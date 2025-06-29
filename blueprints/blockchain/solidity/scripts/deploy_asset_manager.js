// Script de déploiement avancé pour AssetManager (Hardhat)
const hre = require("hardhat");

async function main() {
  const AssetManager = await hre.ethers.getContractFactory("AssetManager");
  const assetManager = await AssetManager.deploy();
  await assetManager.deployed();
  console.log("AssetManager déployé à :", assetManager.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});

module.exports = { deploy_asset_manager };
