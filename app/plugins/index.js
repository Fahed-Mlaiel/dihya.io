// Point d’entrée pour l’enregistrement et la gestion des plugins

export function registerPlugin(plugin) {
  // Ajoute le plugin au système
  console.log(`Plugin enregistré : ${plugin.name}`);
}

export default {
  registerPlugin
};
