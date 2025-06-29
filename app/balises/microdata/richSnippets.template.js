// Template rich snippets
export default function RichSnippets({ headline, datePublished }) {
  return (
    <script type="application/ld+json" dangerouslySetInnerHTML={{
      __html: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'NewsArticle',
        headline,
        datePublished
      })
    }} />
  );
}
