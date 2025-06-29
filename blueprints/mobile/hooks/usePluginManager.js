// Hook métier pour la gestion dynamique des plugins mobile
import { useState } from 'react';

export function usePluginManager() {
  const [plugins, setPlugins] = useState([]);

  const addPlugin = (plugin) => setPlugins(p => [...p, plugin]);
  const removePlugin = (pluginName) => setPlugins(p => p.filter(pl => pl.name !== pluginName));
  const getPlugin = (pluginName) => plugins.find(pl => pl.name === pluginName);

  // Exemple d’intégration dynamique (chargement à la volée)
  const loadPlugin = async (url) => {
    const module = await import(/* @vite-ignore */ url);
    addPlugin({ name: module.name, ...module });
  };

  return { plugins, addPlugin, removePlugin, getPlugin, loadPlugin };
}
