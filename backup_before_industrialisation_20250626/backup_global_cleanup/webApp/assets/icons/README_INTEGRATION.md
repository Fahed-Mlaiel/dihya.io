# Intégration des icônes dans le code

## Exemple React
```js
import IconUser from '../assets/icons/icon-user.svg';

export default function Profil() {
  return <img src={IconUser} alt="Utilisateur" aria-label="Icône utilisateur" />;
}
```

## Exemple Next.js
```js
import Image from 'next/image';
import IconSecurity from '../assets/icons/icon-security.svg';

<Image src={IconSecurity} alt="Sécurité" width={24} height={24} />
```
