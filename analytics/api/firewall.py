# api/firewall.py
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException, Forbidden
import logging
from analytics_module_generator import AnalyticsModuleGenerator

app = Flask(__name__)
analytics_generator = AnalyticsModuleGenerator()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Middleware to check for API key in headers
@app.before_request
def before_request():
    api_key = request.headers.get('X-API-Key')
    if not api_key or api_key != 'YOUR_SECRET_API_KEY':
        raise Forbidden(description="Invalid API key")

# Error handler for Forbidden access
@app.errorhandler(Forbidden)
def handle_forbidden(e):
    return jsonify(error=str(e)), 403

# Endpoint to trigger analytics module generation
@app.route('/generate_analytics_module', methods=['POST'])
def generate_analytics_module():
    data = request.json
    try:
        module_type = data['module_type']
        module_name = data['module_name']
        analytics_generator.generate(module_type, module_name)
        return jsonify(message=f"{module_type} analytics module '{module_name}' generated successfully"), 200
    except KeyError as e:
        return jsonify(error=f"Missing parameter: {e}"), 400
    except Exception as e:
        logging.error(f"Error generating analytics module: {e}")
        return jsonify(error="Internal server error"), 500

if __name__ == '__main__':
    app.run(port=5000)