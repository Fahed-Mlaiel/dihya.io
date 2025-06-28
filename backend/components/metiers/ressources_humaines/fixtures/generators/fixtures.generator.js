// Diese Datei wurde in generators/fixtures.generator.js verschoben.

// fixtures.generator.js - Générateur dynamique de fixtures pour Ressources_humaines

module.exports = {
  generateModel: (name = 'DynamicModel', vertices = 8, faces = 12) => ({
    id: `model-${Math.random().toString(36).substr(2, 6)}`,
    name,
    type: 'mesh',
    vertices: Array(vertices).fill([0,0,0]),
    faces: Array(faces).fill([0,1,2,3]),
    meta: { generated: true, createdAt: new Date().toISOString() }
  }),
  generateUser: (role = 'operator') => ({
    id: `user-${Math.random().toString(36).substr(2, 6)}`,
    name: `User_${role}_${Date.now()}`,
    role
  })
};
