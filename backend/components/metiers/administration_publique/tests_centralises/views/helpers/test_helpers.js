// test_helpers.js
// Tests avancés pour le module views/helpers (centralisation tests)
const helpers = require('../../../views/helpers/views_helper');

describe('Views Helpers Central Tests', () => {
    it('renderTitle génère un titre h1', () => {
        expect(helpers.renderTitle('Dihya')).toBe('<h1>Dihya</h1>');
    });
    it('renderModel génère un bloc modèle', () => {
        expect(helpers.renderModel({ name: 'Cube' })).toBe('<div>Modèle: Cube</div>');
    });
    it('renderError génère un bloc erreur', () => {
        expect(helpers.renderError('Erreur')).toBe("<div class='error'>Erreur</div>");
    });
    it('formatadministration_publiqueDetails préfixe correctement', () => {
        expect(helpers.formatadministration_publiqueDetails('Ultra')).toBe('[administration_publique] Ultra');
    });
    it('renderTitle gère les chaînes vides', () => {
        expect(helpers.renderTitle('')).toBe('<h1></h1>');
    });
    it('renderModel gère les modèles sans nom', () => {
        expect(helpers.renderModel({})).toBe('<div>Modèle: undefined</div>');
    });
    it('renderError gère les messages vides', () => {
        expect(helpers.renderError('')).toBe("<div class='error'></div>");
    });
    it('formatadministration_publiqueDetails gère les détails vides', () => {
        expect(helpers.formatadministration_publiqueDetails('')).toBe('[administration_publique] ');
    });
});
