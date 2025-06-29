// Blueprint modèle métier Asset (Node.js)
// Exemple de classe Asset, instructions d’extension

class Asset {
  constructor(id, name, owner) {
    this.id = id;
    this.name = name;
    this.owner = owner;
  }
}

// Ajouter d’autres modèles métier ici

// Modèle métier AssetModel (Node.js)
class AssetModel {
  constructor(name) {
    this.name = name;
  }
  serialize() {
    return { name: this.name };
  }
}

module.exports = { AssetModel };
