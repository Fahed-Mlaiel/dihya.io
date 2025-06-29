// sample_service.js – Service ultra avancé pour Science (JS)
// Expose endpoints, logique métier, validation, audit, etc.

function helloSample(req, res) {
  res.json({ message: "Hello from Science sample service!" });
}

function validateSample(req, res) {
  if (!req.body || !req.body.value) {
    return res.status(400).json({ error: "Missing value" });
  }
  res.json({ validated: true, input: req.body });
}

module.exports = {
  helloSample,
  validateSample
};
