// Exemple d’intégration des assets de sécurité dans une app React Native
import Lock from '../assets/images/security/icons/lock.svg';
import Shield from '../assets/images/security/icons/shield.svg';
import Login from '../assets/images/security/illustrations/auth/icons/login.svg';

import { Image, View } from 'react-native';

export default function MobileSecurityAssets() {
  return (
    <View>
      <Image source={Lock} accessibilityLabel="Lock" />
      <Image source={Shield} accessibilityLabel="Shield" />
      <Image source={Login} accessibilityLabel="Login" />
    </View>
  );
}
