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
    it('formatRessources_humainesDetails préfixe correctement', () => {
        expect(helpers.formatRessources_humainesDetails('Ultra')).toBe('[ressources_humaines] Ultra');
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
    it('formatRessources_humainesDetails gère les détails vides', () => {
        expect(helpers.formatRessources_humainesDetails('')).toBe('[ressources_humaines] ');
    });
});
