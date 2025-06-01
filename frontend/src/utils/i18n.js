// i18n.js - utilitaire d’internationalisation avancé
/**
 * @file i18n.js
 * @description Utilitaire d’internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 * @i18n (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
 */

const locales = {
  fr: { permission: "Accès refusé", created: "Créé avec succès" },
  en: { permission: "Access denied", created: "Successfully created" },
  ar: { permission: "تم الرفض", created: "تم الإنشاء بنجاح" },
  ber: { permission: "Ulac tazmert", created: "Yettwerru" },
  de: { permission: "Zugriff verweigert", created: "Erfolgreich erstellt" },
  zh: { permission: "拒绝访问", created: "创建成功" },
  ja: { permission: "アクセス拒否", created: "作成に成功しました" },
  ko: { permission: "접근 거부", created: "성공적으로 생성됨" },
  nl: { permission: "Toegang geweigerd", created: "Succesvol aangemaakt" },
  he: { permission: "הגישה נדחתה", created: "נוצר בהצלחה" },
  fa: { permission: "دسترسی رد شد", created: "با موفقیت ایجاد شد" },
  hi: { permission: "पहुंच अस्वीकृत", created: "सफलतापूर्वक बनाया गया" },
  es: { permission: "Acceso denegado", created: "Creado con éxito" }
};

export function getI18n(lang = 'fr') {
  return locales[lang] || locales['fr'];
}
