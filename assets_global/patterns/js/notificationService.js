// notificationService.js – Notifications (UI, mail, webhook)
module.exports = {
  sendNotification: (type, message) => {
    // Exemple métier : notification
    return `Notification [${type}]: ${message}`;
  }
};
