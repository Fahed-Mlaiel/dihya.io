// test_threed.js - Tests unitaires JS pour threed

const assert = require('assert');
const fixtures = require('../fixtures/fixtures');
const validator = require('../utils/validator');

describe('Threed Model Validation', () => {
  it('should validate a correct 3D model', () => {
    assert(validator.isValidModel(fixtures.sample3DModel));
  });

  it('should reject an invalid 3D model', () => {
    assert(!validator.isValidModel({}));
  });
});
