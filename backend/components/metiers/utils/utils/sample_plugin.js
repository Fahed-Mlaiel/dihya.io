// sample_plugin.js – Exemple avancé de plugin pour Environnement (Node.js)
class SamplePlugin {
  run(data) {
    return `Traitement environnemental: ${JSON.stringify(data)}`;
  }
}

module.exports = new SamplePlugin();
