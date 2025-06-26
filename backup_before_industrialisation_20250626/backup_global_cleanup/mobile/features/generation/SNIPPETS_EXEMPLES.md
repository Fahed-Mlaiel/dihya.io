{
  "Generator": {
    "prefix": "generation-generator",
    "body": ["import Generator from './Generator';", "<Generator templateId={1} />"],
    "description": "Exemple d’intégration du générateur de projet"
  },
  "TemplateSelector": {
    "prefix": "generation-template-selector",
    "body": ["import TemplateSelector from './TemplateSelector';", "<TemplateSelector templates={templates} onSelect={setTemplate} />"],
    "description": "Exemple d’intégration du sélecteur de template"
  },
  "GenerationHistory": {
    "prefix": "generation-history",
    "body": ["import GenerationHistory from './GenerationHistory';", "<GenerationHistory history={history} />"],
    "description": "Exemple d’intégration de l’historique des générations"
  }
}
