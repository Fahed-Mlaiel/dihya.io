// Template schema.org
export default function SchemaOrg({ type, name, url }) {
  return (
    <script type="application/ld+json" dangerouslySetInnerHTML={{
      __html: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': type,
        name,
        url
      })
    }} />
  );
}
