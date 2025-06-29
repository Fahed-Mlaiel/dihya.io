// fixtures.js - Fixtures ultra avancés pour le module assurance

module.exports = {
  sampleassuranceModel: {
    id: 'model-001',
    name: 'Cube Ultra',
    vertices: [
      [0,0,0], [1,0,0], [1,1,0], [0,1,0],
      [0,0,1], [1,0,1], [1,1,1], [0,1,1]
    ],
    faces: [
      [0,1,2,3], [4,5,6,7], [0,1,5,4], [2,3,7,6], [1,2,6,5], [0,3,7,4]
    ],
    meta: {
      createdBy: 'test',
      createdAt: new Date().toISOString(),
      tags: ['cube', 'ultra', 'assurance'],
      validated: true
    }
  },
  assets: [
    { id: 'asset-001', type: 'texture', name: 'Texture Bois', url: '/assets/bois.jpg' },
    { id: 'asset-002', type: 'material', name: 'Matériau Métal', url: '/assets/metal.mat' }
  ],
  users: [
    { id: 'user-001', name: 'Alice', role: 'admin' },
    { id: 'user-002', name: 'Bob', role: 'operator' }
  ],
  scenes: [
    {
      id: 'scene-001',
      name: 'Scène Test Ultra',
      models: ['model-001', 'model-002'],
      assets: ['asset-001', 'asset-002'],
      createdBy: 'admin',
      createdAt: new Date().toISOString(),
      meta: { tags: ['scene', 'test', 'ultra'] }
    }
  ],
  errors: [
    { code: 'ERR_MISSING_VERTEX', message: 'Le modèle assurance est incomplet.' },
    { code: 'ERR_INVALID_ASSET', message: 'Asset non reconnu.' }
  ],
  edgeCases: {
    emptyModel: { id: 'empty', name: '', vertices: [], faces: [], meta: {} },
    hugeModel: {
      id: 'huge',
      name: 'GigaMesh',
      vertices: Array(10000).fill([0,0,0]),
      faces: Array(5000).fill([0,1,2]),
      meta: { tags: ['huge', 'stress'] }
    }
  }
};

// Diese Datei wurde in models/fixtures.js verschoben.
