// Exemple d’intégration complète : login → dashboard → génération → export → audit
import { useAuth } from '../hooks';
import { getMarketplaceItems } from '../services/marketplaceService';
import { hasPermission } from '../security/permissionUtils';
import { detectLocale } from '../i18n/localeUtils';

export async function fullUserFlow() {
  // 1. Authentification
  const { login, user } = useAuth();
  await login('demo@dihya.io', 'password');

  // 2. Dashboard : récupération des items du marketplace
  const items = await getMarketplaceItems();

  // 3. Génération de contenu (exemple : achat d’un template)
  const achat = items.length ? await buyItem(items[0].id) : null;

  // 4. Export (mocké)
  const exportData = achat ? JSON.stringify(achat) : null;

  // 5. Audit de sécurité
  const isAdmin = hasPermission(user, 'admin');

  // 6. Détection de la langue
  const locale = detectLocale('fr-FR,fr;q=0.9');

  return { user, items, achat, exportData, isAdmin, locale };
}
