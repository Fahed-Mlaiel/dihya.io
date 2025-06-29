// db.js – Mock DB ultra avancé pour l’API Beaute (JS)
const db = {
  findById: (id) => ({ id, name: 'Cube Ultra', status: 'active' }),
  insert: (data) => ({ ...data, id: 2 }),
  update: (id, data) => ({ ...data, id }),
  delete: () => true
};

module.exports = db;
