# plugins/examplePlugin/__init__.py
from .analytics_backend import AnalyticsBackend
from .analytics_frontend import AnalyticsFrontend
from .analytics_plugin import AnalyticsPlugin
from .analytics_docs import AnalyticsDocs
from .analytics_i18n import AnalyticsI18n

class ExamplePlugin:
    def __init__(self):
        self.backend = AnalyticsBackend()
        self.frontend = AnalyticsFrontend()
        self.plugin = AnalyticsPlugin()
        self.docs = AnalyticsDocs()
        self.i18n = AnalyticsI18n()

    def setup(self):
        """Setup the analytics modules."""
        self.backend.setup()
        self.frontend.setup()
        self.plugin.setup()
        self.docs.setup()
        self.i18n.setup()

    def start(self):
        """Start the analytics modules."""
        self.backend.start()
        self.frontend.start()
        self.plugin.start()
        self.docs.start()
        self.i18n.start()

# This would be the entry point for the plugin system to load this plugin.
def load_plugin():
    example_plugin = ExamplePlugin()
    example_plugin.setup()
    example_plugin.start()
    return example_plugin

# If the plugin is being run as a standalone module, initialize it.
if __name__ == "__main__":
    load_plugin()