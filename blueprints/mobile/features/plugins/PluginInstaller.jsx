import React from 'react';
// Installation de plugins via l’UI
export default function PluginInstaller({ onInstall }) {
  const [pluginName, setPluginName] = React.useState('');
  return (
    <form onSubmit={e => {e.preventDefault();onInstall && onInstall(pluginName);}}>
      <input value={pluginName} onChange={e=>setPluginName(e.target.value)} placeholder='Nom du plugin' />
      <button type='submit'>Installer</button>
    </form>
  );
}
