// db.js – Mock DB ultra avancé pour l’API Threed (JS)
const db = {
  findById: (table, id) => ({ id, name: 'Cube Ultra', status: 'active' }),
  insert: (table, data) => ({ ...data, id: 2 }),
  update: (table, id, data) => ({ ...data, id }),
  delete: (table, id) => true
};
// Les variables 'table' et 'id' sont nécessaires pour l'API, mais ne sont pas utilisées directement ici.
// eslint-disable-next-line no-unused-vars
const table = undefined;
// eslint-disable-next-line no-unused-vars
const id = undefined;
// eslint-disable-next-line no-unused-vars
module.exports = db;
