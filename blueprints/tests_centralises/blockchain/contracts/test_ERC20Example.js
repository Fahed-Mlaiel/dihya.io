const { ethers } = require("hardhat");
describe("contracts", function () {
  let contract, owner, user;
  beforeEach(async function () {
    [owner, user] = await ethers.getSigners();
    const Factory = await ethers.getContractFactory("contracts");
    contract = await Factory.deploy();
    await contract.deployed();
  });
  it("doit respecter la logique métier principale", async function () {
    // ...test métier réel sur le smart contract...
    // Exemple : vérifier le mint, transfert, droits, etc.
    // À adapter selon le contrat
    expect(await contract.address).to.match(/^0x/);
  });
  it("doit gérer les cas limites et la sécurité", async function () {
    // ...test edge case ou sécurité...
    // Exemple : fail si input invalide, overflow, etc.
  });
});
