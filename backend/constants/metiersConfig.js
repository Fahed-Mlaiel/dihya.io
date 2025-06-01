// src/constants/metiersConfig.js
/**
 * Configuration des métiers (VR, AR, IA, etc.) pour Dihya Coding
 * @module src/constants/metiersConfig.js
 */
export const METIERS = [
  {
    key: 'vr_ar',
    label: {
      fr: 'Réalité Virtuelle / Augmentée',
      en: 'Virtual / Augmented Reality',
      ar: 'الواقع الافتراضي / المعزز',
      ber: 'Tigawt Tazwart / Tazwart n Tazwart',
      de: 'Virtuelle / Erweiterte Realität',
      zh: '虚拟/增强现实',
      ja: 'バーチャル/拡張現実',
      ko: '가상/증강 현실',
      nl: 'Virtuele / Augmented Reality',
      he: 'מציאות מדומה / רבודה',
      fa: 'واقعیت مجازی / افزوده',
      hi: 'आभासी / संवर्धित वास्तविकता',
      es: 'Realidad Virtual / Aumentada',
    },
    roles: ['admin', 'user', 'guest'],
    plugins: true,
    ai: true,
    graphql: true,
    rgpd: true,
  },
  // ... autres métiers ...
];
