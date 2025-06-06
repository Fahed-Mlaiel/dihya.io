// sample_fixture.js - Fixtures avancés JS pour Threed

module.exports = {
  sample: {
    name: 'Sample',
    type: 'test',
    vertices: 8,
    faces: 12,
    createdBy: 'unit-test',
    createdAt: new Date().toISOString(),
    tags: ['test', '3d', 'sample']
  },
  cubeUltra: {
    id: 'model-001',
    name: 'Cube Ultra',
    type: 'mesh',
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
      tags: ['cube', 'ultra', '3d']
    }
  },
  pyramidPro: {
    id: 'model-002',
    name: 'Pyramide Pro',
    type: 'mesh',
    vertices: [
      [0,0,0], [1,0,0], [0.5,1,0], [0.5,0.5,1]
    ],
    faces: [
      [0,1,2], [0,1,3], [1,2,3], [2,0,3]
    ],
    meta: {
      createdBy: 'test',
      createdAt: new Date().toISOString(),
      tags: ['pyramide', 'pro', '3d']
    }
  }
};
