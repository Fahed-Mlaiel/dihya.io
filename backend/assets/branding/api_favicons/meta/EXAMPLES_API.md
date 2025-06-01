# Dihya API Favicon – Exemples API REST/GraphQL

## REST (OpenAPI)
```http
GET /api/meta/favicon?lang=fr
```

## GraphQL
```graphql
query {
  faviconMeta(lang: "fr") {
    name
    description
    accessibility {
      contrast
      altText
    }
    rgpd {
      conformite
      anonymisation
      exportable
    }
    seo {
      robots
      sitemap
    }
    plugins
    audit {
      last_audit
      result
    }
  }
}
```
