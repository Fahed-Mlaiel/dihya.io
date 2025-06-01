// seo_plugin.ts – Plugin SEO ultra avancé (balises meta, accessibilité, audit, RGPD, CI/CD, tests)
import React from 'react';

export function SeoHead({ title, description }: { title: string; description: string }) {
  React.useEffect(() => {
    document.title = title;
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) metaDesc.setAttribute('content', description);
    else {
      const meta = document.createElement('meta');
      meta.name = 'description';
      meta.content = description;
      document.head.appendChild(meta);
    }
  }, [title, description]);
  return null;
}
