// Template de balises OpenGraph
export default function OpenGraphTags({ title, image, url }) {
  return (
    <>
      <meta property="og:title" content={title} />
      <meta property="og:image" content={image} />
      <meta property="og:url" content={url} />
    </>
  );
}
