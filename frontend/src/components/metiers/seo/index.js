// Dihya SEO Module - index.js
// SEO avancé, multilingue, sécurisé, auditable, RGPD, multitenant, fallback open source
// Compatible React, Next.js, Vue, SSR, CI/CD, Codespaces
// @module SEO

/**
 * Génère les balises SEO dynamiques multilingues et logs structurés.
 * @param {Object} options - { lang, title, description, url, image, type, tenant, role }
 * @returns {JSX.Element}
 */
export function SeoMeta({ lang = 'fr', title, description, url, image, type = 'website', tenant = 'default', role = 'guest' }) {
  // Internationalisation dynamique
  const translations = {
    fr: { robots: 'index, follow', },
    en: { robots: 'index, follow', },
    ar: { robots: 'فهرسة, متابعة', },
    de: { robots: 'index, follow', },
    zh: { robots: '索引, 跟随', },
    ja: { robots: 'インデックス, フォロー', },
    ko: { robots: '색인, 팔로우', },
    nl: { robots: 'index, follow', },
    he: { robots: 'אינדקס, עקוב', },
    fa: { robots: 'فهرست, دنبال کردن', },
    hi: { robots: 'अनुक्रमणिका, अनुसरण', },
    es: { robots: 'indexar, seguir', },
    am: { robots: 'ⴰⵎⵙⵙⴰⵏ, ⴰⵎⵎⴰⵣⵉⵏ', },
  };
  const metaRobots = translations[lang]?.robots || translations['fr'].robots;
  // Logs SEO structurés (exemple)
  if (typeof window !== 'undefined') {
    window.dihyaSEOLog = window.dihyaSEOLog || [];
    window.dihyaSEOLog.push({ lang, title, url, tenant, role, timestamp: new Date().toISOString() });
  }
  return (
    <>
      <title>{title}</title>
      <meta name="description" content={description} />
      <meta name="robots" content={metaRobots} />
      <meta property="og:title" content={title} />
      <meta property="og:description" content={description} />
      <meta property="og:url" content={url} />
      <meta property="og:image" content={image} />
      <meta property="og:type" content={type} />
      {/* JSON-LD multilingue */}
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': type,
        name: title,
        description,
        url,
        image,
        inLanguage: lang,
        publisher: tenant,
        audience: role,
      }) }} />
    </>
  );
}

/**
 * Appel API backend pour logs SEO/auditabilité (exemple, à adapter selon backend)
 * @param {Object} logData
 */
export async function logSeoEvent(logData) {
  try {
    await fetch('/api/seo/log', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(logData),
      credentials: 'include',
    });
  } catch (e) {
    // Fallback local log
    if (typeof window !== 'undefined') {
      window.dihyaSEOLog = window.dihyaSEOLog || [];
      window.dihyaSEOLog.push({ ...logData, fallback: true });
    }
  }
}

// Tests unitaires et intégration : voir __tests__/seo.test.js
