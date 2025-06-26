// Hooks custom event threed (Node.js)
function beforeCustomEvent(event, data) {
  // Logique avant événement custom
  return { event, data };
}
function afterCustomEvent(event, data) {
  // Logique après événement custom
  return { event, data };
}
module.exports = { beforeCustomEvent, afterCustomEvent };
