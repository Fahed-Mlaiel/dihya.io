from flask import Flask
from flask_restful import Api
from .analytics_backend import AnalyticsBackend
from .analytics_frontend import AnalyticsFrontend
from .analytics_plugins import AnalyticsPlugins
from .analytics_docs import AnalyticsDocs
from .analytics_i18n import AnalyticsI18n
from .security import configure_security

# Initialize Flask application
app = Flask(__name__)
api = Api(app)

# Configure security settings
configure_security(app)

# Initialize analytics modules
backend = AnalyticsBackend()
frontend = AnalyticsFrontend()
plugins = AnalyticsPlugins()
docs = AnalyticsDocs()
i18n = AnalyticsI18n()

# Register API resources
api.add_resource(backend, '/api/analytics/backend')
api.add_resource(frontend, '/api/analytics/frontend')
api.add_resource(plugins, '/api/analytics/plugins')
api.add_resource(docs, '/api/analytics/docs')
api.add_resource(i18n, '/api/analytics/i18n')

if __name__ == '__main__':
    app.run(debug=False)  # Set to False in production