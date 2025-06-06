/* global console */
// sample_admin.js
// Exemple d'utilisation des admin views (JS)
const admin = require('../admin/admin_views');
console.log(admin.getAdminDashboard ? admin.getAdminDashboard() : 'Admin dashboard sample');
