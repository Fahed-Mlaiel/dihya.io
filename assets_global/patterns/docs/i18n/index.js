// Point d’entrée JS pour l’i18n patterns docs
// Permet d’importer dynamiquement les fichiers de traduction selon la langue

const i18n = {
  ar: require('./i18n_ar.json'),
  ar_dz: require('./i18n_ar_dz.json'),
  ar_eg: require('./i18n_ar_eg.json'),
  ar_ma: require('./i18n_ar_ma.json'),
  ar_tn: require('./i18n_ar_tn.json'),
  ber: require('./i18n_ber.json'),
  ber_cha: require('./i18n_ber_cha.json'),
  ber_kab: require('./i18n_ber_kab.json'),
  ber_rif: require('./i18n_ber_rif.json'),
  ber_tac: require('./i18n_ber_tac.json'),
  ber_tou: require('./i18n_ber_tou.json'),
  ber_tzm: require('./i18n_ber_tzm.json'),
  de: require('./i18n_de.json'),
  en: require('./i18n_en.json'),
  en_gb: require('./i18n_en_gb.json'),
  en_us: require('./i18n_en_us.json'),
  es: require('./i18n_es.json'),
  fr: require('./i18n_fr.json'),
  fr_ca: require('./i18n_fr_ca.json'),
  hi: require('./i18n_hi.json'),
  it: require('./i18n_it.json'),
  ja: require('./i18n_ja.json'),
  ko: require('./i18n_ko.json'),
  nl: require('./i18n_nl.json'),
  pl: require('./i18n_pl.json'),
  pt: require('./i18n_pt.json'),
  ru: require('./i18n_ru.json'),
  sw: require('./i18n_sw.json'),
  tr: require('./i18n_tr.json'),
  uk: require('./i18n_uk.json'),
  zh: require('./i18n_zh.json'),
};

module.exports = i18n;
