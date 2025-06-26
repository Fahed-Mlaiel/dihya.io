// Hooks notification threed (Node.js)
function beforeNotificationSend(data) {
  // Logique avant envoi de notification
  return data;
}
function afterNotificationSend(data) {
  // Logique après envoi de notification
  return data;
}
module.exports = { beforeNotificationSend, afterNotificationSend };
