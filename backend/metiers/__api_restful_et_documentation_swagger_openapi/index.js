// Module métier : __api_restful_et_documentation_swagger/openapi
// Fournit endpoints RESTful, documentation Swagger/OpenAPI, sécurité, plugins, etc.

const express = require('express');
const router = express.Router();
const swaggerUi = require('swagger-ui-express');
const YAML = require('yamljs');
const openapiDocument = YAML.load('openapi.yaml');

router.use('/docs', swaggerUi.serve, swaggerUi.setup(openapiDocument));

router.get('/metiers', (req, res) => {
  // Endpoint RESTful exemple (GET)
  res.json({ metiers: ['accessibilité', 'api', 'automatisation', 'déploiement'] });
});

// TODO: Ajouter sécurité, plugins, audit, RGPD, GraphQL, etc.

module.exports = router;
