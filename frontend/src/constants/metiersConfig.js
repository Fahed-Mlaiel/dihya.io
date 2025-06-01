// metiersConfig.js - Configuration des métiers Dihya Coding
/**
 * @fileoverview Configuration des modules métiers (IA, VR, AR, voyage, plugins, sécurité, i18n)
 * @author Dihya Coding
 * @version 1.0.0
 * @license MIT
 */

export const METIERS = [
  {
    key: 'voyage',
    label: {
      fr: 'Voyage', en: 'Travel', ar: 'السفر', de: 'Reise', zh: '旅行', ja: '旅行', ko: '여행', nl: 'Reis', he: 'טיול', fa: 'سفر', hi: 'यात्रा', es: 'Viaje', amazigh: 'ⴰⵙⴳⴰⵙ'
    },
    roles: ['admin', 'user'],
    enabled: true,
    plugin: false
  },
  {
    key: 'vr_ar',
    label: {
      fr: 'VR/AR', en: 'VR/AR', ar: 'الواقع الافتراضي/المعزز', de: 'VR/AR', zh: '虚拟现实/增强现实', ja: 'VR/AR', ko: 'VR/AR', nl: 'VR/AR', he: 'VR/AR', fa: 'واقعیت مجازی/افزوده', hi: 'वीआर/एआर', es: 'VR/AR', amazigh: 'VR/AR'
    },
    roles: ['admin', 'user'],
    enabled: true,
    plugin: true
  },
  // ...autres métiers extensibles
];
