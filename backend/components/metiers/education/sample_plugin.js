// sample_plugin.js – Plugin-Template pour Education (Dihya Coding)
module.exports = function educationSamplePlugin({ i18n, audit, user, data }) {
  audit.log({ event: 'plugin_invoked', user, data });
  if (!user || user.role !== 'admin') throw new Error(i18n('access_denied'));
  // ... Logique plugin ...
  return { success: true, message: i18n('plugin_success') };
};
