// Template de balises <meta>
export default function MetaTags({ description, keywords }) {
  return (
    <>
      <meta name="description" content={description} />
      <meta name="keywords" content={keywords} />
    </>
  );
}
