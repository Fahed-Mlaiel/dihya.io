// views.js - Exemple métier principal views
function renderView(viewName, context) {
  return `<div>${viewName}: ${JSON.stringify(context)}</div>`;
}
module.exports = renderView;
