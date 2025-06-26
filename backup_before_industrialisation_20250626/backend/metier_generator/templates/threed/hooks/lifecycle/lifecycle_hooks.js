// Hooks lifecycle threed (Node.js)
function beforeLifecycleEvent(event, data) {
  // Logique avant événement de cycle de vie
  return { event, data };
}
function afterLifecycleEvent(event, data) {
  // Logique après événement de cycle de vie
  return { event, data };
}
module.exports = { beforeLifecycleEvent, afterLifecycleEvent };
