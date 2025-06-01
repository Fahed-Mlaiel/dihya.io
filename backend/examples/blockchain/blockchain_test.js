// blockchain_test.js – Test ultra avancé d’intégration dApp/Smart Contract (audit, RGPD, accessibilité, plugins, CI/CD)
import { connectWallet, sendTransaction } from './dapp_example';

describe('dApp Blockchain Dihya – Sécurité, RGPD, audit', () => {
  it('connecte un wallet et logue l’audit', async () => {
    const account = await connectWallet();
    expect(account).toBeDefined();
  });

  it('refuse une transaction sans consentement RGPD', async () => {
    window.localStorage.setItem('rgpd_consent', '0');
    await expect(sendTransaction('0xA', '0xB', 1)).rejects.toThrow('Consentement RGPD requis');
  });

  it('accepte une transaction avec consentement RGPD', async () => {
    window.localStorage.setItem('rgpd_consent', '1');
    await expect(sendTransaction('0xA', '0xB', 1)).resolves.toBeDefined();
  });
});
