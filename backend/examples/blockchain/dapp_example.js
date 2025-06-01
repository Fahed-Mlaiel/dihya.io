// dapp_example.js – Exemple ultra avancé d’intégration dApp Web3 (auth, audit, RGPD, i18n, plugins, accessibilité, tests, CI/CD)
import Web3 from 'web3';
import { AuditLogger } from '../plugins/audit_plugin';
import { checkConsent } from '../plugins/rgpd_plugin';

export async function connectWallet() {
  if (!window.ethereum) throw new Error('Wallet non détecté');
  const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
  AuditLogger.log('wallet_connect', 'dapp', { user: accounts[0] });
  return accounts[0];
}

export async function sendTransaction(from, to, value) {
  if (!checkConsent()) throw new Error('Consentement RGPD requis');
  const web3 = new Web3(window.ethereum);
  const tx = await web3.eth.sendTransaction({ from, to, value });
  AuditLogger.log('transaction', 'dapp', { from, to, value });
  return tx;
}
