// api_samples.js – Exemples d’intégration API (Node.js)
function sampleApiRequest() {
  return {
    method: 'POST',
    url: '/api/secure-endpoint',
    headers: { Authorization: 'Bearer <token>' },
    body: { data: 'example' }
  };
}
module.exports = { sampleApiRequest };
