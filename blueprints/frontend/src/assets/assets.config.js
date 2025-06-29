// Configuration centralisée des assets

export const assetConfig = {
  theme: {
    primaryColor: '#0055B7',
    secondaryColor: '#007A3D',
    font: 'Open Sans, Arial, sans-serif'
  },
  i18n: require('./i18n.assets.json'),
  accessibility: {
    defaultAlt: {
      fr: 'Image par défaut',
      en: 'Default image',
      ar: 'الصورة الافتراضية'
    }
  }
};
