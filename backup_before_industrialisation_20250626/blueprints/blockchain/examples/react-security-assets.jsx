// Exemple d’intégration des assets de sécurité dans un composant React
import { SecurityIcons } from '../assets/images/security';
import { AuditSvg, Auth, Firewall } from '../assets/images/security/illustrations';

export default function SecurityAssetsDemo() {
  return (
    <div>
      <h2>Security Icons</h2>
      <img src={SecurityIcons.Lock} alt="Lock" />
      <img src={SecurityIcons.Shield} alt="Shield" />
      <img src={SecurityIcons.Warning} alt="Warning" />
      <img src={SecurityIcons.Key} alt="Key" />
      <img src={SecurityIcons.Privacy} alt="Privacy" />
      <h2>Auth Illustrations</h2>
      <img src={Auth.AuthIcons.Login} alt="Login" />
      <img src={Auth.AuthIcons.TwoFA} alt="2FA" />
      <h2>Firewall Illustration</h2>
      <img src={Firewall.Firewall} alt="Firewall" />
      <h2>Audit Illustration</h2>
      <img src={AuditSvg} alt="Audit" />
    </div>
  );
}
